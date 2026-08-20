import requests
import json

r = requests.get('https://news.orz.ai/api/v1/dailynews/',
                 params = {'platform':'zhihu'},
                 timeout=10)
print('状态码：',r.status_code)
print('正文：',r.text)

data = r.json()

# 写入文件,T：成功，F：失败
def write_file(data):
    try:
        with open("api_date.json","w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
        return True
    except OSError:
        return False
    
write_file(data)