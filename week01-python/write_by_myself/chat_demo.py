import os
from openai import OpenAI


def main():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("没读到 DEEPSEEK_API_KEY。请在当前终端先执行：")
        print('$env:DEEPSEEK_API_KEY="你的sk-..."')
        return

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com",
    )

    response = client.chat.completions.create(
        model="deepseek-chat",  # 若报模型不存在，改成控制台/文档里的当前模型名
        messages=[
            {"role": "user", "content": "你好，用一句话介绍你自己"}
        ],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
