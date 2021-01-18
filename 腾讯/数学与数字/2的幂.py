'''
2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 2**0 = 1
示例 2:

输入: 16
输出: true
解释: 2**4 = 16
示例 3:

输入: 218
输出: false

考查标签  位运算、数学
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 1:
            return True
        if str(n)[-1] not in ['2','4','6','8']:
            return False
        while n >1:
            if n%2 == 0:
                n = n//2
            else:
                return False
        return True