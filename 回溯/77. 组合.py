# coding:utf-8
'''
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


# 回溯法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []

        def backrace(index):
            if len(path) == k:
                res.append(path[:])
            for i in range(index, n):
                path.append(nums[i])
                backrace(i + 1)
                path.pop()

        nums = [i for i in range(1, n + 1)]
        res = []
        path = []
        backrace(0)
        return res


'''
知识点：
组合和排列的区别在于，组合是无序的，排列是有序的
'''
