from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from db_todos import init_db, insert_todo, update_todo, select_todos, delete_todo


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