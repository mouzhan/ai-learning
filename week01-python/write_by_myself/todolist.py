todolists = []  # 必须在循环外：只创建一次，添加的内容才能留下来

while True:
    print("1.添加 2.列表 3.修改 4.删除 5.完成 6.退出")
    print("请输入数字来选择对应的功能：")
    option = input().strip()

    # 添加
    if option == "1":
        # 待办内容是文字，不要 int，也不要套在「必须是数字」的校验里
        print("请输入要添加的待办：")
        user_input = input()
        todolists.append(user_input)
        print("已添加")

    # 展示列表
    elif option == "2":
        print(todolists)
    
    # 修改
    elif option == "3":
        if not todolists:  # 空列表用这个判断，不要用 != None
            print("暂无待办事项，先去添加几个吧😊")
            continue
        for i, m in enumerate(todolists):
            print(f"第{i+1}条待办，是{m}")
        try:
            change_index = int(input("请输入对应待办的序号来更改待办🙂："))
            todolists[change_index - 1] = input("请输入新的内容：")
            print(todolists)
        except ValueError:
            print("序号请输入数字")
        except IndexError:
            print("序号超出范围")

    # 删除
    elif option == "4":
        if not todolists:
            print("暂无待办事项，先去添加几个吧😊")
            continue
        for index, item in enumerate(todolists):
            print(f"第{index+1}条待办，是{item}")
        try:
            delete_index = int(input("请输入对应待办的序号来删除待办🙂："))
            todolists.pop(delete_index - 1)
            print("已删除")
            print(todolists)
        except ValueError:
            print("序号请输入数字")
        except IndexError:
            print("序号超出范围")

    # 完成
    elif option == "5":
        if not todolists:
            print("暂无待办事项，去添加几个吧🙂")
            continue
        for a, b in enumerate(todolists):
            print(f"第{a+1}条待办，是{b}")
        try:
            finish_index = int(input("请输入序号选择要完成的待办💃："))
            i = finish_index - 1
            todolists[i] = "[√]" + todolists[i]
            print(todolists)
        except ValueError:
            print("序号请输入数字")
        except IndexError:
            print("序号超出范围")

    # 退出
    elif option == "6":
        print("谢谢🙇")
        break

    else:
        print("请输入菜单上的数字 1～6")
