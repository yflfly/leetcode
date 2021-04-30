'''
1523. 在区间范围内统计奇数数目
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
示例 1：
输入：low = 3, high = 7
输出：3
解释：3 到 7 之间奇数数字为 [3,5,7] 。
示例 2：
输入：low = 8, high = 10
输出：1
解释：8 到 10 之间奇数数字为 [9] 。
'''


# 枚举会出现超时问题
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            if i % 2 != 0:
                res += 1
        return res


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = (high - low) // 2
        if low % 2 == 0 and high % 2 == 0:
            return n
        else:
            return n + 1
