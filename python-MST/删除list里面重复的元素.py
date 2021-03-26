# coding:utf-8

# 方法一:
a = [1, 2, 4, 2, 4, 5, 6, 5, 7, 8, 9, 0]
print(list(set(a)))
'''
[0, 1, 2, 4, 5, 6, 7, 8, 9]
'''

# 方法二:
b = {}
b = b.fromkeys(a)
print(b)
c = list(b.keys())
print(c)
'''
{1: None, 2: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 0: None}
[1, 2, 4, 5, 6, 7, 8, 9, 0]
'''
