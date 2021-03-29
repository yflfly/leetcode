'''
全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
相关标签  回溯算法
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        backtrack(nums, [])
        return res
'''
代码讲解的网址：
https://leetcode-cn.com/problems/permutations/solution/46-quan-pai-lie-hui-su-fa-by-jue-qiang-z-jym3/
'''