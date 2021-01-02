'''
面试题 05.06. 整数转换
整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。

示例1:
 输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
 输出：2
示例2:
 输入：A = 1，B = 2
 输出：2
'''
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A & 0xffffffff) ^ (B & 0xffffffff)).count('1')


'''
解题思路：
A&0xFFFFFFFF，B&0xFFFFFFFF将A,B转化为无符号数
'''