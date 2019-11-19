dic_student = {}
for i in range(5):
    name = input("请输入姓名：")
    age = input("请输入年龄")
    dic_student[name] = age
for k, v in dic_student.items():
    print("{0:{2}<10}{1}".format(k, v, chr(12288)))
