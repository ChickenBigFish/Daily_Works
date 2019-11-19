sec_code = {"John": "123", "Marry": "111", "Tommy": "123456"}
user_name = input("请输入用户名：")
user_code = input("请输入密码：")
if user_name not in sec_code:
    print("用户名不正确！")
elif sec_code[user_name] != user_code:
    print("密码不正确！")
else:
    print("密码正确！")
