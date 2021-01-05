'''
子集
给你一个整数数组 nums ，返回该数组所有可能的子集（幂集）。解集不能包含重复的子集。
示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：
输入：nums = [0]
输出：[[],[0]]
'''


# 方法一:动态规划
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]
        for i in nums:
            dp = dp + [[i] + num for num in dp]
        return dp


# 方法二：递归
class Solution(object):
    def subsets(self, nums):
        if nums == []:
            return [[]]
        return self.subsets(nums[:-1]) + [i + [nums[-1]] for i in self.subsets(nums[:-1])]
