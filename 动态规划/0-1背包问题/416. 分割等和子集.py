'''
416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
'''


# 会报错误
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 != 0:  # 奇数 无法均分两份
            return False
        target = target % 2  # 走到这一步就是偶数，除半
        # 二维数组，行数n是物品索引（不包含 no item），列数target+1 （包含0）
        dp = [[False] * (target + 1) for _ in range(n)]
        dp[0][0] = True
        # 第0行，第一个数恰好只能让容积为它的背包恰好装满
        # 所以最终dp数组的第0行只有dp[0][0]和dp[0][nums[0]]是true，其他都是默认的初始值false
        if nums[0] <= target:  # 单个数不能超过 target
            dp[0][nums[0]] = True

        for i in range(1, n):  # [1,..., n-1]
            for j in range(0, target + 1):  # [0, target]
                if (j < nums[i]):  # 容量太小
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[-1][-1]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:  # 奇数 无法均分两份
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


'''
0-1 背包问题选取的物品的容积总量 不能超过 规定的总量；
本题选取的数字之和需要 恰好等于 规定的和的一半。
这一点区别，决定了在初始化的时候，所有的值应该初始化为 false。
作为「0-1 背包问题」，它的特点是：「每个数只能用一次」。
解决的基本思路是：物品一个一个选，容量也一点一点增加去考虑，这一点是「动态规划」的思想，特别重要。
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/416-fen-ge-deng-he-zi-ji-dong-tai-gui-hu-csk5/
'''

'''
特例：如果和为奇数，那一定找不到符合要求的子集，返回False
dp[j]:有没有子集和为j的子集，有为True，没有为False
初始化dp数组：长度为target + 1，用于存储子集的和从0到target是否可能取到的情况。比如和为0一定可以取到（也就是子集为空），那么dp[0] = True。
'''

'''
复杂度分析
时间复杂度：O(n∗target)
空间复杂度：O(target)
'''
