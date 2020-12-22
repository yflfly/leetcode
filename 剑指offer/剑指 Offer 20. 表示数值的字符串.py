# coding:utf-8
'''
剑指 Offer 20. 表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

'''


# 自己的解法
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if float(s):
                return True
            else:
                return True
        except:
            return False
# 官方的解法
