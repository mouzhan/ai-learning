import random



# # 支持重来一次版
# while True:
#     right_number = random.randint(1,100)
#     count = 0
#     # 玩一次版
#     while True:
#         try:
#             user_input = int(input("请输入数字，看看是否心有灵犀："))
#             if 1 <= user_input <= 100:
#                 count += 1
#                 if user_input > right_number:
#                     print("猜大了")
#                     continue
#                 elif user_input < right_number:
#                     print("猜小了")
#                     continue
#                 else:
#                     print("恭喜你，猜对了🎉，用了" + str(count) + "次")
#                     break
#             else:
#                 print("请输入1~100的数字(●'◡'●)")
#         except ValueError:
#             print("请输入1~100的数字(●'◡'●)")
#     again = input("要不要再来一次？（输入“是”重来一次，或者任意键退出🙂）")
#     if again != "是":
#         print("再见！")
#         break


def play_one_round():
    right_number = random.randint(1,100)
    count = 0

    while True:
        try:
            user_input = int(input("请输入数字，看看是否心有灵犀："))
            if 1 <= user_input <= 100:
                count += 1
                if user_input > right_number:
                    print("猜大了")
                    continue
                elif user_input < right_number:
                    print("猜小了")
                    continue
                else:
                    print("恭喜你猜对了🎉，用了" + str(count) +"次")
                    break
            else:
                print("请输入1~100之间的数字(●'◡'●)")
        except ValueError:
            print("请输入1~100之间的数字(●'◡'●)")


while True:
    play_one_round()
    again = input("要不要再来一次？输入“是”重来一次，或者按任意键退出：")
    if again != "是":
        print("再见")
        break