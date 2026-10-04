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

         



# 检索_关键词重叠
def search_chunks(chunks, questions, top_n = 3):
    # 保留中文
    keep_chinese = re.sub(r'[^\u4e00-\u9fa5]', '', questions)
    # 生成所有相邻二字组
    nearby_two = [keep_chinese[i:i+2] for i in range(len(keep_chinese)-1)]
    remove_values = ['林冲','冲的']
    for i in remove_values:
        while i in nearby_two:
            nearby_two.remove(i)
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