def count_items(items:list[str]) -> dict[str, int]:
    results:dict[str, int] = {}
    for x in items:
        results[x]=results.get(x,0)+1
    return results

def top_n(counter:dict[str, int], n:int=2) -> list[tuple[str, int]]:
    return sorted(counter.items(), key=lambda kv: kv[1], reverse=True)[:n]

def filter_by_keyword(items,keyword:str) -> list[str]:
    return [x for x in items if keyword in x]

if __name__ == "__main__":
    data = ["登录", "支付", "登录", "搜索", "支付", "登录"]
    items = ["登陆成功","登陆失败","支付成功","支付失败","搜索成功","搜索失败"]
    c = count_items(data)
    print(c)
    print(top_n(c))
    print(filter_by_keyword(items, "成功"))