import re

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
    for chunk in chunks:
        chunk = chunk.strip()
     # 如果 i 为空、为 0、为 None、为 False，就执行
        if not chunk:
             continue
         # 清理---     
        if re.fullmatch(r'[-/*_]+', re.sub(r'\s+', '', chunk)):
              continue
        if len(chunk) < min_len:
              pending += chunk + "\n" 
              continue
        if len(chunk) >= min_len:
              if pending:
                  chunk = pending + chunk
                  pending = ''
              merged.append(chunk)
    if pending:
        merged.append(pending)
         
    return merged

         



# 检索_关键词重叠
def search_chunks(chunks, questions, top_n = 3):
    # 保留中文
    keep_chinese = re.sub(r'[^\u4e00-\u9fa5]', '', questions)
    # 生成所有相邻二字组
    nearby_two = [keep_chinese[i:i+2] for i in range(len(keep_chinese)-1)]
    collection = []
    for chunk in chunks:
        score = 0
        for two in nearby_two:
            if two in chunk:
                score += 1
        collection.append((score, chunk))       
    return sorted(collection, key=lambda x: x[0],reverse=True)[:top_n]


# 提示词demo
def prompt_demo(list, question):
    prompt = '只根据下面资料回答，不要编资料里没有的内容。\n'
    for i,(score,text) in enumerate(list,start=1):
        prompt += f'\n【资料{i}】\n{text}\n'
    prompt += '\n问题：' + question + '答完要写用了【资料几】'
    return prompt