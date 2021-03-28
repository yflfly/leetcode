# coding:utf-8
dic = {"name": "zs", "age": 18}
print(dic)  # {'name': 'zs', 'age': 18}

# 删除键
del dic['name']

print(dic)  # {'age': 18}
dic2 = {"name": "ls"}
# update合并字典
dic.update(dic2)
print(dic)  # {'age': 18, 'name': 'ls'}
