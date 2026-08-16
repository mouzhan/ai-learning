import random

def guess_answer(answer):
    count = 0
    while True:
        guess = int(input("猜数字："))
        try:
            if 1 <= guess <= 100:
                count += 1
                if count == answer:
                    break
                elif count > answer:
                    print("猜大了")
                    continue
                elif count < answer:
                    print("猜小了")
                    continue
        except ValueError:
            return "请输入1~100的整数(●'◡'●)"
        
right_answer = random.randint(1,100)
guess_answer(right_answer)