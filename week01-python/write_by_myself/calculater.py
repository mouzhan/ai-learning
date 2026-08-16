# while True:
#     try:
#         input_once = input("请输入第一个数：").strip()
#         option = input("请输入运算符（+ - * /）：").strip()
#         input_twice = input("请输入第二个数：").strip()

#         # 兼容中文输入法下的全角符号
#         fullwidth = {"＋": "+", "－": "-", "＊": "*", "×": "*", "／": "/", "÷": "/"}
#         option = fullwidth.get(option, option)

#         a = float(input_once)
#         b = float(input_twice)

#         if option == "+":
#             answer = a + b
#         elif option == "-":
#             answer = a - b
#         elif option == "*":
#             answer = a * b
#         elif option == "/":
#             if b == 0:
#                 print("除数不能为 0")
#                 continue
#             answer = a / b
#         else:
#             print("运算符无效，你输入的是：", repr(option))
#             print("请只输入这四个之一：+ - * /")
#             continue

#         print("结果：", answer)

#         again = input("再算一次？（输入“是”继续，其它键退出）：").strip()
#         if again != "是":
#             print("再见！")
#             break
#     except ValueError:
#         print("数字无效。请分三次输入，例如：")
#         print("  第一个数：8")
#         print("  运算符：+")
#         print("  第二个数：2")
#         print("不要写成 8+2 一次输入。")

# 抽函数版本
def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return None  # 用 None 表示算失败，让外面决定怎么提示
        return a / b
    else:
        return None  # 非法运算符


# 只有直接运行本文件时才进交互；被测试脚本 import 时不会卡住等输入
if __name__ == "__main__":
    while True:
        try:
            input_once = input("请输入第一个数：").strip()
            option = input("请输入运算符（+ - * /）：").strip()
            input_twice = input("请输入第二个数：").strip()

            # 兼容中文输入法：全角/特殊符号 → 半角 + - * /
            fullwidth = {"＋": "+", "－": "-", "＊": "*", "×": "*", "／": "/", "÷": "/"}
            option = fullwidth.get(option, option)

            a = float(input_once)
            b = float(input_twice)
            # 关键：把转换后的 a、b、option 传进去，不要传原来的字符串
            answer = calculate(a, option, b)
            if answer is None:
                print("算不了：除数为 0，或运算符不是 + - * /")
                continue

            print("结果：", answer)

            again = input("再算一次？（输入“是”继续，其它键退出）：")
            if again == "是":
                continue
            break

        except ValueError:
            print("数字无效。请分三次输入，例如：")
            print("  第一个数：8")
            print("  运算符：+")
            print("  第二个数：2")
            print("不要写成 8+2 一次输入。")

