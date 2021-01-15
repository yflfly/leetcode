'''
子集
给你一个整数数组 nums ，返回该数组所有可能的子集（幂集）。解集不能包含重复的子集。
示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：
输入：nums = [0]
输出：[[],[0]]
提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10


考查标签：位运算、数组、回溯算法
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        res = []
        n = len(nums)
        helper(0, [])
        return res


