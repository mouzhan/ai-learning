from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from db_todos import init_db, insert_todo, update_todo, select_todos, delete_todo
from chat_def import chat
from rag_def import read_chunks_file, split_by_blank_line, clean_chunks, search_chunks, prompt_demo
from pathlib import Path


app = FastAPI()
@app.get("/")
def hello():
    return {"message":"ok"}

# 初始化
init_db()

@app.get("/todos")
def get_todos():
    return select_todos()
# 继承的写法
class TodoIn(BaseModel):
    text:str
class TodoUpdate(BaseModel):
    n:int
    text:str
class TodoDelete(BaseModel):
    n:int
class ChatAI(BaseModel):
    text:str
class RagChat(BaseModel):
    question:str

# 退到 week01-python 文件夹
FILE_DIR = Path(__file__).resolve().parent.parent
# 文档
file_path = FILE_DIR.parent / "knowledge" / "林冲.md"

@app.post("/todos")
# 定义一个函数 create_todo，它接收一个叫 item 的参数，并且这个参数预期是 TodoIn 类型。
def create_todo(item:TodoIn):
    ok = insert_todo(item.text)
    if not ok:
        # raise 触发异常
        raise HTTPException(status_code=500, detail="写入失败")
    return True

@app.post("/update_todos")
def update_lists(item:TodoUpdate):
    result = update_todo(item.text, item.n)
    if result == 0:
        raise HTTPException(status_code=400, detail="序号不存在")
    return True

@app.post("/delete_todos")
def delete_lists(item:TodoDelete):
    result = delete_todo(item.n)
    if result == 0:
        raise HTTPException(status_code=400, detail="序号不存在")
    return True

@app.post("/chat")
def chat_ai(item:ChatAI):
    reply = chat(item.text)    
    if reply is False:
        raise HTTPException(status_code=500, detail="请设置环境变量")
    return {"reply":reply}

@app.post("/rag")
def rag_chat(item:RagChat):
    text = read_chunks_file(file_path)
    if text == None:
        raise HTTPException(status_code=400, detail="空文件")
    if text == False:
        raise HTTPException(status_code=500, detail="请检查路径是否正确")
    chunks = split_by_blank_line(text)
    chunks = clean_chunks(chunks, min_len = 30)
    key_words_score = search_chunks(chunks,item.question,top_n=3)
    sources = []
    for source in key_words_score:
        sources.append(source[1][:40])
    prompt_test = prompt_demo(key_words_score, item.question)
    reply = chat(prompt_test)
    if reply is False:
        raise HTTPException(status_code=500, detail="请检查key是否正确")
    return {"reply":reply, "sources":sources}