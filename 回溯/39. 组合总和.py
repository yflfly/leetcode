# coding:utf-8
'''
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 结果列表
        ans = []
        # 可能的组合
        tmp = []

        def helper(idx, total):
            """回溯，求组合总和
            Args:
                idx: 选取元素索引
                total: 组合中的元素和
            """
            # 基准条件
            # 当元素和大于目标值，直接返回
            if total > target:
                return
            # 当元素和等于目标值，将组合添加到结果中，返回
            if total == target:
                ans.append(tmp[::])
                return
            # 进入分支，同时避免重复组合
            for i in range(idx, len(candidates)):
                # 更新 total 值，
                total += candidates[i]
                # 同时将当前元素尝试添加到组合中
                tmp.append(candidates[i])
                # 再次进入递归
                # 这里可以看文章图例，递归向下，可选元素是从自身开始选择
                # 这里同时也能避免组合重复，因为不会再次选择索引 i 前面对应的元素
                helper(i, total)
                # 回溯，回退组合元素及 total 值
                tmp.pop()
                total -= candidates[i]

        total = 0
        helper(0, total)
        return ans

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []

        def helper(idx, total):
            if total > target:
                return
            if total == target:
                ans.append(tmp[::])
                return
            for i in range(idx, len(candidates)):
                total += candidates[i]
                tmp.append(candidates[i])
                helper(i, total)
                tmp.pop()
                total -= candidates[i]

        total = 0
        helper(0, total)
        return ans