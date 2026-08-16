import json


todolists = []

# 添加待办
def add_todo(todos,todo):
    todos.append(todo)
    return todos

# 展示待办
def list_todos(todos):
    return todos

# 修改待办
# 约定n是数字，外边限制一下非法输入
def update_todo(todos,n,todo):
    # 空列表--还是在外边判断吧，要不然白改了
    # if not todos:
    #     return None
    # 越界
    if not (1 <= n <= len(todos)):
        return False
    # 参数是列表、序号、更新后的待办,然后根据索引改元素内容
    todos[n - 1] = todo
    return todos
 

# 删除待办，注意用户输入的比索引多1
# 约定n是数字，外边限制一下非法输入
def delete_todo(todos,n):
    # 空列表--还是在外边判断吧，没有数据何谈删除
    # if not todos:
    #     return None
    # 越界
    if not (1 <= n <= len(todos)):
        return False
    # 根据索引删除
    todos.pop(n - 1)
    return todos

# 完成待办
def finish_todo(todos,n):
    # 空列表--还是在外边判断吧，没有数据何谈完成
    # if not todos:
    #     return None
    # 越界
    if not (1 <= n <= len(todos)):
        return False
    # 根据序号完成
    todos[n - 1] = todos[n - 1] + "[已完成]"
    return todos


# 写入文件,T：成功，F：失败
def write_file(todos):
    try:
        with open("todolists.json","w",encoding="utf-8") as f:
            json.dump(todos,f,ensure_ascii=False,indent=2)
        return True
    except OSError:
        return False


# 读取文件,成功返回列表，none为没有文件，false为非法文件
def read_file():
    try:
        with open("todolists.json","r",encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return False







