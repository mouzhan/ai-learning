from fastapi import FastAPI
from todolist_def import add_todo, list_todos, write_file, read_file
from pydantic import BaseModel
from fastapi import HTTPException


app = FastAPI()
@app.get("/")
def hello():
    return {"message":"ok"}


data = read_file()

todos = data if isinstance(data,list) else []

@app.get("/todos")
def get_todos():
    return list_todos(todos)
# 继承的写法
class TodoIn(BaseModel):
    text:str

@app.post("/todos")
# 定义一个函数 create_todo，它接收一个叫 item 的参数，并且这个参数预期是 TodoIn 类型。
def create_todo(item:TodoIn):
    add_todo(todos,item.text)
    ok = write_file(todos)
    if not ok:
        raise HTTPException(status_code=500, detail="写入失败")
    return todos