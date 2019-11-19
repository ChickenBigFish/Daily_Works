dic_student = {}
for i in range(5):
    Class = input("请输入班级：")
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    length = input("请输入身高：")
    weight = input("请输入体重：")
    dic_student[(Class, name)] = [age, length, weight]
for k, v in dic_student.items():
    print("{0:<5}{1:{2}<5}".format(k[0], k[1], chr(12288)), end="")
    print("{:<5}{:<8}{:<8}".format(v[0], v[1], v[2]))
