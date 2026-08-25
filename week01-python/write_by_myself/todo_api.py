from fastapi import FastAPI
from todolist_def import add_todo, list_todos, write_file, read_file, update_todo, delete_todo
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
class TodoUpdate(BaseModel):
    n:int
    text:str
class TodoDelete(BaseModel):
    n:int

@app.post("/todos")
# 定义一个函数 create_todo，它接收一个叫 item 的参数，并且这个参数预期是 TodoIn 类型。
def create_todo(item:TodoIn):
    add_todo(todos,item.text)
    ok = write_file(todos)
    if not ok:
        # raise 触发异常
        raise HTTPException(status_code=500, detail="写入失败")
    return todos

@app.post("/update_todos")
def update_lists(item:TodoUpdate):
    result = update_todo(todos,item.n,item.text)
    if result is False:
        raise HTTPException(status_code=400, detail="序号不存在")
    ok = write_file(todos)
    if not ok:
        raise HTTPException(status_code=500, detail="修改失败")
    return todos

@app.post("/delete_todos")
def delete_lists(item:TodoDelete):
    result = delete_todo(todos,item.n)
    if result is False:
        raise HTTPException(status_code=400, detail="序号不存在")
    ok = write_file(todos)
    if not ok:
        raise HTTPException(status_code=500, detail="删除失败")
    return todos