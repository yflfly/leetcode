'''
633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：
输入：c = 3
输出：false
示例 3：
输入：c = 4
输出：true
示例 4：
输入：c = 2
输出：true
示例 5：
输入：c = 1
输出：true
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c ** 0.5)
        while a <= b:
            tmp = a ** 2 + b ** 2
            if tmp == c:
                return True
            if tmp < c:
                a += 1
            if tmp > c:
                b -= 1
        return False
