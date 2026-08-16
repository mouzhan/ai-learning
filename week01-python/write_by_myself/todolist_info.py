from todolist_def import add_todo
from todolist_def import update_todo

from todolist_def import list_todos
from todolist_def import delete_todo
from todolist_def import finish_todo

from todolist_def import write_file
from todolist_def import read_file


def main():
    data = read_file()
    if data is False:
        print("非json文件，请确认格式")
        return
    elif isinstance(data, list):
        todolists = data
    else:
        todolists = []

    while True:
        try:
            print("1.添加 2.列表 3.修改 4.删除 5.完成 6.退出")
            print("请输入数字来选择对应的功能：")
            option = input().strip()
            # 添加待办
            if option == "1":
                user_input = input("请输入待办😊：")
                add_todo(todolists, user_input)
                a = write_file(todolists)
                if a == True:
                    print("添加成功")
                else:
                    print("添加失败")
            # 展示列表
            elif option == "2":
                print(list_todos(todolists))
            # 修改待办
            elif option == "3":
                if not todolists:
                    print("暂无待办事项，先去添加几个吧😊")
                    continue
                for i, m in enumerate(todolists):
                    print(f"第{i + 1}条待办，是{m}")
                user_index = int(input("请输入对应待办的序号来更改待办🙂："))
                new_todo = input("请输入新的待办😊：")
                results = update_todo(todolists, user_index, new_todo)
                if results is False:
                    print("请选择已有的待办序号😊")
                else:
                    a = write_file(results)
                    if a == True:
                        print("修改成功")
                        print(todolists)
                    else:
                        print("修改失败")

            # 删除待办
            elif option == "4":
                if not todolists:
                    print("暂无待办事项，先去添加几个吧😊")
                    continue
                for a, b in enumerate(todolists):
                    print(f"第{a + 1}条待办，是{b}")
                delete_index = int(input("请输入对应待办的序号来删除待办🙂："))
                results = delete_todo(todolists, delete_index)
                if results is False:
                    print("请选择已有的待办序号😊")
                else:
                    a = write_file(results)
                    if a == True:
                        print("删除成功")
                        print(todolists)
                    else:
                        print("删除失败")
            # 完成待办
            elif option == "5":
                if not todolists:
                    print("暂无待办事项，先去添加几个吧😊")
                    continue
                for i, k in enumerate(todolists):
                    print(f"第{i + 1}条待办，是{k}")
                finish_index = int(input("请输入序号选择要完成的待办💃："))
                results = finish_todo(todolists, finish_index)
                if results is False:
                    print("请选择已有的待办序号😊")
                else:
                    a = write_file(results)
                    if a == True:
                        for i, m in enumerate(todolists):
                            print(f"第{i + 1}条待办，{m}")
                    else:
                        print("结束待办失败...!")
            # 退出
            elif option == "6":
                a = write_file(todolists)
                if a == True:
                    print("文件写入成功(●'◡'●)")
                else:
                    print("文件写入失败！")

                break
            # 防非数字输入
            else:
                print("请输入菜单上的数字 1～6")
        except ValueError:
            print("请输入数字🙂")


if __name__ == "__main__":
    main()
