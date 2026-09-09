import sqlite3  # 导入标准库：用 Python 操作 SQLite


DB_PATH = "todos.db"  # 数据库文件名；一个 .db 文件就是一个库


# 建库：其实是「打开/创建文件 + 建表」；文件不存在时 connect 会创建
def init_db():
    # 连接 todos.db；with 结束时会自动关闭连接，成功则提交、失败则回滚
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()  # 游标：专门负责执行 SQL
        # 下面三引号里是 SQL，不能写 Python 的 # 注释（SQLite 会报 unrecognized token: "#"）
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY,
            content TEXT
            )"""
        )
        conn.commit()  # 把建表结果写进磁盘（with 成功退出时通常也会提交）


# 添加待办：往 todos 表插入一行
def insert_todo(content: str):
    with sqlite3.connect(DB_PATH) as conn:  # 每次调用连一次同一个库
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO todos(content) VALUES (?)",  # ? 是占位符，防拼接 SQL
            (content,),  # 一元组：把参数 content 填进那个 ?
        )
        return cursor.lastrowid  # 返回刚插入那一行的 id（自动编号）


# # 展示待办
def select_todos():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, content FROM todos"
        )
        return cursor.fetchall()

# 修改待办
def update_todo(content, n):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE todos SET content = ? WHERE id = ?",(content, n)
        )
        return cursor.rowcount

# 删除待办
def delete_todo(n):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM todos WHERE id = ?",(n,)
        )
        return cursor.rowcount