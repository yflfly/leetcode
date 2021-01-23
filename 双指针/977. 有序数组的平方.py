'''
977. 有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

考查标签 双指针
'''

# 方法一
'''
先对数组中的每一个数进行平方和，然后再进行排序
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for each in nums:
            res.append(each * each)
        res.sort()
        return res


# 方法二：双指针
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for each in nums]
        left = 0
        right = len(nums) - 1
        pos = len(nums) - 1  # 从后面开始填充结果数组
        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res[pos] = nums[left] * nums[left]
                left += 1
            else:
                res[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return res
'''
代码讲解网址：
https://leetcode-cn.com/problems/squares-of-a-sorted-array/solution/you-xu-shu-zu-de-ping-fang-by-leetcode-solution/
'''