"""
自动测 calculate：不用手动 input。
在本目录运行：python test_calculater.py
"""

from calculater import calculate


def check(name, got, expected):
    if got != expected:
        raise AssertionError(f"[{name}] 期望 {expected!r}，实际 {got!r}")
    print(f"OK  {name}")


# --- 正常四则 ---
check("加", calculate(8, "+", 2), 10)
check("减", calculate(8, "-", 2), 6)
check("乘", calculate(8, "*", 2), 16)
check("除", calculate(8, "/", 2), 4.0)

# --- 边界 ---
check("除零", calculate(8, "/", 0), None)
check("非法运算符", calculate(8, "^", 2), None)
check("小数", calculate(0.1, "+", 0.2), 0.1 + 0.2)  # float 本身的精度行为
check("负数", calculate(-3, "*", 2), -6)

print("全部通过")
