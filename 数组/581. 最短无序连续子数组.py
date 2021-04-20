'''
581. 最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。
示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
示例 2：
输入：nums = [1,2,3,4]
输出：0
示例 3：
输入：nums = [1]
输出：0
'''


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp = nums.copy()
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < len(nums):
            if nums[left] != tmp[left]:
                break
            left += 1
        while right > left:
            if nums[right] != tmp[right]:
                break
            right -= 1

        return right - left + 1
