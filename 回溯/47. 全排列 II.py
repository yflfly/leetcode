# coding:utf-8
'''
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            dic = set()
            for i in range(first, n):
                if nums[i] in dic:
                    continue  # 重复，因此剪枝
                dic.add(nums[i])
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        res = []
        def backtrack(nums, path):
            if not nums and path not in res:
                res.append(path)
            
            for i in range(len(nums)):
                cur = nums[i]
                backtrack(nums[:i] + nums[i+1:], path + [cur])
        backtrack(nums, [])
        return res
'''