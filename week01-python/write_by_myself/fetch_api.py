import requests
import json


def write_file(data):
    try:
        with open("api_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except OSError:
        return False


def main():
    r = requests.get(
        "https://news.orz.ai/api/v1/dailynews/",
        params={"platform": "zhihu"},
        timeout=10,
    )
    if r.status_code != 200:
        print("请求失败", r.status_code, r.text)
        return

    print("状态码：", r.status_code)
    data = r.json()
    new_data = data["data"]
    top_three = new_data[:3]

    file = write_file(top_three)
    if file is False:
        print("写出失败！")
    else:
        print("写入成功")


if __name__ == "__main__":
    main()
