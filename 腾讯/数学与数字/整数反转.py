'''
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1：
输入：x = 123
输出：321
示例 2：
输入：x = -123
输出：-321
示例 3：
输入：x = 120
输出：21
示例 4：
输入：x = 0
输出：0

考查标签： 数学
'''


class Solution:
    def reverse(self, x: int) -> int:
        max1 = 2 ** 31 - 1
        min1 = - 2 ** 31
        if x < 0:
            flag = -1
        else:
            flag = 1
        str1 = list(str(abs(x)))
        int1 = ''.join(str1[::-1])
        if flag * int(int1) > max1 or flag * int(int1) < min1:
            return 0

        return flag * int(int1)
