dic_country = {"China": "Beijing",
               "American": "Washington",
               "Norway": "Oslo",
               "Japan": "Tokyo",
               "Germany": "Berlin",
               "Canada": "Ottawa",
               "France": "Paris",
               "Thailand": "Bangkok"}
country = input("请输入要查询的国家：")
country = country.lower()
country = country.title()
print(dic_country.get(country, "未查询到该国家名！"))
