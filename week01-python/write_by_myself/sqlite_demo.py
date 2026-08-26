import sqlite3

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()

cursor.execute("""   
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        content TEXT
    )"""
 
)
conn.commit()
print('==========新增数据==========')
cursor.execute("INSERT INTO todos(content) VALUES (?)", ("哈哈哈哈",))
cursor.execute("INSERT INTO todos(content) VALUES (?)", ("keep moving",))

conn.commit()

print("=========查询数据==========")
cursor.execute("SELECT * FROM todos")
all_todos = cursor.fetchall()
print(all_todos)
conn.commit()