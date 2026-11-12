import re
import math
from sentence_transformers import SentenceTransformer

# 读文档函数
def read_chunks_file(file_path):
        try:
            with open(file_path,"r",encoding="utf-8") as f:
                text = f.read()
                if not text:
                    return None
                return text
        except FileNotFoundError:
             return False


# 按照空行切
def split_by_blank_line(text):
    paragraphs = re.split(r'\n\s*\n',text)
    return [p.strip() for p in paragraphs if p.strip()]


# 清洗垃圾段
def clean_chunks(chunks,min_len = 30):
    merged = []
    pending = ''
    # 标题是否已经贴到过长段上。写在循环外面，避免每读一段就被重置成 False
    used = False
    for chunk in chunks:
        chunk = chunk.strip()
        # 空段：丢掉
        if not chunk:
             continue
        # 分隔线（如 ---）：丢掉，不当成标题
        if re.fullmatch(r'[-/*_]+', re.sub(r'\s+', '', chunk)):
              continue
        # 短标题：还没贴过长段就叠加上去；已经贴过就换掉旧标题
        if len(chunk) < min_len:
              if used == False:
                   pending += chunk + "\n" 
              else:
                   pending = chunk + "\n"
                   used = False 
              continue
        # 长段：有标题就拼在前面，不要清空 pending，拼完把 used 改成 True
        if len(chunk) >= min_len:
              if pending:
                  chunk = pending + chunk
                  used = True
                #   pending = ''
              merged.append(chunk)
    # 循环结束时，还没贴出去的短标题单独收进来
    if pending and not used:
        merged.append(pending)
         
    return merged

         
# 检索：余弦 + 少见二字加权，返回前 top_n 个 (分数, 正文)
def search_chunks(chunks, questions, top_n = 3):
    collection = []
    question_embedding = text_to_embedding(questions)
    for chunk in chunks:
        chunk_embedding = text_to_embedding(chunk)
        sim = cosine_similarity(question_embedding, chunk_embedding)
        collection.append((sim, chunk))
    # 分数从高到低排，取前几名
    return sorted(collection, key=lambda x: x[0],reverse=True)[:top_n]


# 每个二字出现在几段里 → 权重 = 总段数 / 段数。越少见越大（改为向量之后已经包含，用不上了）
# def bigram_weights(chunks):
#     # 每个二字出现在多少段里
#     df = {}
#     for chunk in chunks:
#         keys = text_to_dict(chunk)
#         # 这段里出现过的二字，段数加 1；同一段里出现多次也只加一次
#         for key in keys:
#             df[key] = df.get(key, 0) + 1
#     total = len(chunks)
#     weights = {}
#     for key, count in df.items():
#         # 例：30 段里 2 段有「结局」→ 权重 15；几乎每段都有「林冲」→ 权重约 1
#         weights[key] = total / count
#     return weights

# 加载模型
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


# 一段文字变成向量
def text_to_embedding(text):
    # 把文本编码成向量
    vector = model.encode(text)
    return vector


# 相似度：比较问题和某一段各自的二字次数字典，返回小数
def cosine_similarity(question_embedding, chunk_embedding):
    # 三个累加量先写成 0，第一次 += 才有旧值可读
    mol = 0
    den_before_sqrt_a = 0
    den_before_sqrt_b = 0
    # 分子
    for i in range(len(question_embedding)):
        mol += question_embedding[i] * chunk_embedding[i]
    # 分母左边
    for value in question_embedding:
        den_before_sqrt_a += value*value
        den_a = math.sqrt(den_before_sqrt_a)
    # 分母右边
    for value in chunk_embedding:
        den_before_sqrt_b += value*value
        den_b = math.sqrt(den_before_sqrt_b)
    # 分母是两边长度相乘；相似度 = 分子 / 分母
    den = den_a * den_b
    return mol / den



# 提示词demo
def prompt_demo(list, question):
    prompt = '只根据下面资料回答，不要编资料里没有的内容。\n'
    for i,(score,text) in enumerate(list,start=1):
        prompt += f'\n【资料{i}】\n{text}\n'
    prompt += '\n问题：' + question + '答完要写用了【资料几】'
    return prompt