# day01-basic.py 知识点详解

对应源码：`week01-python/day01-basic.py`

本文按「整段代码在做什么 → 逐段拆解 → 知识点清单」组织，覆盖该文件涉及的全部 Python 基础。

---

## 1. 整段代码在做什么

这是一个迷你「行为频次分析」脚本：

1. `count_items`：统计列表里每个字符串出现了多少次
2. `top_n`：从统计结果里取出出现次数最高的前 n 项
3. `if __name__ == "__main__":`：直接运行本文件时，用示例数据演示上述两个函数

示例数据：

```python
["登录", "支付", "登录", "搜索", "支付", "登录"]
```

期望结果（在 `count_items` 正确、`n=2` 时）：

```text
{'登录': 3, '支付': 2, '搜索': 1}
[('登录', 3), ('支付', 2)]
```

---

## 2. 源码全文（对照阅读）

```python
def count_items(items: list[str]) -> dict[str, int]:
    results: dict[str, int] = {}
    for x in items:
        results[x] = results.get(x, 0) + 1
    return results

def top_n(counter: dict[str, int], n: int = 2) -> list[tuple[str, int]]:
    return sorted(counter.items(), key=lambda kv: kv[1], reverse=True)[:n]

if __name__ == "__main__":
    data = ["登录", "支付", "登录", "搜索", "支付", "登录"]
    c = count_items(data)
    print(c)
    print(top_n(c))
```

---

## 3. `count_items`：频次统计

### 3.1 函数在做什么

遍历字符串列表，用字典记录「每个元素 → 出现次数」，最后返回该字典。

### 3.2 函数定义与类型注解（Type Hints）

```python
def count_items(items: list[str]) -> dict[str, int]:
```

| 写法 | 含义 |
|------|------|
| `def 函数名(...):` | 定义函数 |
| `items: list[str]` | 参数 `items` 应为「字符串列表」 |
| `-> dict[str, int]` | 返回值应为「键是 str、值是 int 的字典」 |

要点：

- 类型注解**不改变运行逻辑**，主要给人和工具（IDE、mypy 等）看
- `list[str]`、`dict[str, int]` 是 Python 3.9+ 的写法；更老版本可用 `from typing import List, Dict` 再写 `List[str]`、`Dict[str, int]`
- 注解写错不会立刻报错，但静态检查工具会提示

### 3.3 字典（dict）基础

```python
results: dict[str, int] = {}
```

- `{}` 创建空字典
- 字典用「键 → 值」存数据，查找平均很快
- `results[x] = ...`：键不存在则新建，存在则覆盖
- 本例中：键是行为名（如 `"登录"`），值是出现次数

常见操作：

```python
d = {}
d["登录"] = 1          # 赋值
print(d["登录"])       # 取值；键不存在会 KeyError
print(d.get("支付", 0)) # 安全取值；没有则返回默认值 0
"登录" in d            # 判断键是否存在 → True/False
```

### 3.4 `dict.get(key, default)` —— 计数的核心技巧

```python
results[x] = results.get(x, 0) + 1
```

含义：

1. 取当前 `x` 的已有次数；若还没有这个键，当作 `0`
2. 加 `1`
3. 写回字典

等价的「啰嗦写法」：

```python
if x in results:
    results[x] += 1
else:
    results[x] = 1
```

为什么推荐 `get`：

- 更短，意图清晰
- 避免直接 `results[x]` 在键不存在时触发 `KeyError`

### 3.5 `for` 循环遍历列表

```python
for x in items:
    ...
```

- 依次取出列表中的每个元素，赋给 `x`
- 不需要下标时，优先用这种写法
- 需要下标时可用 `for i, x in enumerate(items):`

### 3.6 `return` 与缩进（作用域）

Python 用**缩进**决定代码属于哪一层：

```python
# 正确：先循环完，再返回
for x in items:
    results[x] = results.get(x, 0) + 1
return results

# 错误：return 缩进在 for 里 → 第一次循环就退出
for x in items:
    results[x] = results.get(x, 0) + 1
    return results  # 只会统计第一个元素
```

`return` 一旦执行，函数立即结束，后面的循环不会再跑。

### 3.7 逐步推演

输入：`["登录", "支付", "登录"]`

| 步骤 | `x` | `results` 变化 |
|------|-----|----------------|
| 初始 | — | `{}` |
| 1 | `"登录"` | `{"登录": 1}` |
| 2 | `"支付"` | `{"登录": 1, "支付": 1}` |
| 3 | `"登录"` | `{"登录": 2, "支付": 1}` |

---

## 4. `top_n`：取最高频的前 n 项

### 4.1 函数在做什么

从频次字典中，按次数从大到小排序，取出前 `n` 个 `(元素, 次数)`。

### 4.2 默认参数

```python
def top_n(counter: dict[str, int], n: int = 2) -> list[tuple[str, int]]:
```

- `n: int = 2`：调用时可不传 `n`，默认取 Top 2
- `top_n(c)` 等价于 `top_n(c, 2)`
- 也可显式传入：`top_n(c, 3)`

注意：

- 默认参数应放在参数列表**靠后**的位置
- 可变对象（如 `[]`、`{}`）作默认参数容易踩坑；本例用的是不可变的 `int`，安全

### 4.3 返回类型：`list[tuple[str, int]]`

- `tuple[str, int]`：二元组，第 1 个是 `str`，第 2 个是 `int`
- 整体是「这种元组」组成的列表
- 例如：`[("登录", 3), ("支付", 2)]`

元组（tuple）要点：

- 用圆括号表示，如 `("登录", 3)`
- 有序、不可变（创建后不能改元素）
- 适合表示「固定结构的一对/一组值」

### 4.4 `dict.items()`

```python
counter.items()
```

- 返回「键值对视图」，每个元素形如 `(key, value)`
- 例：`{"登录": 3, "支付": 2}.items()` → 类似 `[("登录", 3), ("支付", 2)]`（顺序在 3.7+ 按插入序）

相关：

| 方法 | 得到什么 |
|------|----------|
| `.keys()` | 所有键 |
| `.values()` | 所有值 |
| `.items()` | 所有 (键, 值) |

### 4.5 `sorted()` 排序

```python
sorted(counter.items(), key=lambda kv: kv[1], reverse=True)
```

| 参数 | 作用 |
|------|------|
| 第一个参数 | 要排序的可迭代对象 |
| `key=...` | 用什么规则比大小 |
| `reverse=True` | 降序（大 → 小）；默认升序 |

要点：

- `sorted` 返回**新列表**，不修改原数据
- 列表自身的 `.sort()` 会原地修改；这里用 `sorted` 更适合「算完就用」的链式写法

### 4.6 `lambda` 匿名函数

```python
key=lambda kv: kv[1]
```

含义：定义一个临时小函数——接收 `kv`，返回 `kv[1]`（即次数）。

等价于：

```python
def get_count(kv):
    return kv[1]

sorted(counter.items(), key=get_count, reverse=True)
```

何时用 `lambda`：

- 函数很短、只用一次（尤其是传给 `key=`、`map`、`filter` 等）
- 逻辑复杂时，仍应写成普通 `def`，可读性更好

`kv` 是一对，如 `("登录", 3)`：

- `kv[0]` → `"登录"`（键）
- `kv[1]` → `3`（值/次数）

### 4.7 切片 `[:n]`

```python
...[:n]
```

- `lst[:n]`：取前 n 个元素（下标 0 到 n-1）
- `n` 大于列表长度时**不报错**，有多少取多少
- 其他常见切片：`lst[1:]`（去掉第一个）、`lst[-1]`（最后一个）、`lst[::-1]`（反转）

### 4.8 一行组合关系

```text
counter.items()
    → sorted(..., key=按次数, reverse=True)   # 降序排好
    → [:n]                                    # 截取前 n 名
```

这是 Python 里很常见的 **Top-N** 写法：排序 + 切片。

### 4.9 逐步推演

输入：`counter = {"登录": 3, "支付": 2, "搜索": 1}`，`n=2`

1. `items()` → `[("登录", 3), ("支付", 2), ("搜索", 1)]`
2. 按 `kv[1]` 降序 → `[("登录", 3), ("支付", 2), ("搜索", 1)]`
3. `[:2]` → `[("登录", 3), ("支付", 2)]`

---

## 5. 程序入口：`if __name__ == "__main__":`

### 5.1 这段在做什么

只有「直接运行本文件」时才执行演示代码：准备数据 → 统计 → 打印 → 取 Top-N → 再打印。

### 5.2 `__name__` 是什么

每个 `.py` 文件都有内置变量 `__name__`：

| 运行方式 | `__name__` 的值 | 入口块是否执行 |
|----------|-----------------|----------------|
| 直接运行本文件（如 `python day01-basic.py`） | `"__main__"` | 执行 |
| 被其他文件 `import` | 模块名（如文件名相关字符串） | 不执行 |

作用：把「可复用的函数」和「演示/测试代码」分开。别人只想用 `count_items` / `top_n` 时，不会顺带跑 `print`。

### 5.3 变量与函数调用

```python
data = ["登录", "支付", "登录", "搜索", "支付", "登录"]
c = count_items(data)
print(c)
print(top_n(c))
```

| 概念 | 说明 |
|------|------|
| 列表字面量 | `[...]` 直接写出列表内容 |
| 赋值 | `c = ...` 把返回值存起来，后面复用 |
| 函数调用 | `函数名(参数)` |
| 默认参数生效 | `top_n(c)` 未传 `n`，使用定义处的默认值 |

为什么先赋给 `c` 再打印：避免写两次 `count_items(data)`，少做一次重复统计。

### 5.4 `print()`

- 把对象转成可读字符串，输出到控制台
- 字典、列表、元组都能直接 `print`，Python 用默认格式显示

---

## 6. 三个部分如何串起来

```text
data（行为列表）
    │
    ▼
count_items  ──►  c（频次字典）
    │
    ▼
top_n(c)     ──►  最高频的前 n 项列表
    │
    ▼
print 两次，在终端看到结果
```

| 部分 | 角色 |
|------|------|
| `count_items` | 统计 |
| `top_n` | 排序截取 Top-N |
| `if __name__ == "__main__":` | 本地演示入口 |

---

## 7. 知识点速查表

| 类别 | 知识点 | 在本文件中的位置 |
|------|--------|------------------|
| 函数 | `def`、参数、`return` | 全文 |
| 类型注解 | `list[str]`、`dict[str, int]`、`tuple[str, int]`、`->` | 两个函数签名 |
| 字典 | 创建、赋值、作为计数器 | `count_items` |
| 字典方法 | `.get(key, default)`、`.items()` | 两个函数 |
| 循环 | `for x in items` | `count_items` |
| 缩进/作用域 | `return` 必须在循环外 | `count_items` |
| 默认参数 | `n: int = 2` | `top_n` |
| 排序 | `sorted(..., key=..., reverse=True)` | `top_n` |
| 匿名函数 | `lambda kv: kv[1]` | `top_n` |
| 切片 | `[:n]` | `top_n` |
| 元组 | `(键, 值)` 对 | `top_n` 返回值 |
| 模块入口 | `if __name__ == "__main__":` | 文件底部 |
| 输出 | `print` | 入口块 |
| 列表 | 字面量、遍历 | 入口块 + `count_items` |

---

## 8. 常见易错点

1. **`return` 缩进进 `for`**：只统计第一个元素就退出。
2. **直接用 `results[x] + 1` 而键还不存在**：会 `KeyError`；应先用 `get(x, 0)`。
3. **搞混升序/降序**：要「最高频」必须 `reverse=True`。
4. **`key` 写错成 `kv[0]`**：会按字符串本身排序，而不是按次数。
5. **以为类型注解会强制检查**：运行时通常不强制；要靠工具或自己保证。
6. **把演示代码写在模块顶层（没有 `if __name__`）**：一被 import 就会执行 `print`。

---

## 9. 可自行扩展的练习

1. 把 `n` 改成 `3`，观察输出变化。
2. 用 `collections.Counter` 重写 `count_items`，对比写法。
3. 次数相同时，让 `top_n` 再按字符串名字排序（稳定/多关键字排序）。
4. 把入口块改成从键盘 `input` 读入若干词再统计。

---

## 10. 一句话总结

本文件用「字典 + `get`」做计数，用「`sorted` + `lambda` + 切片」做 Top-N，再用 `if __name__ == "__main__"` 作为可独立运行的演示入口——覆盖了 Python 入门阶段最常用的一批语法与习惯写法。
