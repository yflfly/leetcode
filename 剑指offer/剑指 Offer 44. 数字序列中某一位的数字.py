# coding:utf-8
'''
剑指 Offer 44. 数字序列中某一位的数字
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
 
限制：
0 <= n < 2^31
'''
# 下面的方法会超时间限制
class Solution:
    def findNthDigit(self, n: int) -> int:
        str1 = ''
        for i in range(n+1):
            str1 = str1+str(i)
        return int(list(str1)[n])

# 对数字进行规律的查找
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.