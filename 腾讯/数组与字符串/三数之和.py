# coding:utf-8
'''
三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：
输入：nums = []
输出：[]
示例 3：
输入：nums = [0]
输出：[]
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3 or not nums:
            return []
        nums_sorted = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            if nums_sorted[i] == nums_sorted[i - 1] and i > 0:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum1 = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
                if sum1 < 0:
                    left += 1
                elif sum1 > 0:
                    right -= 1
                else:
                    res.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                    while left < right and nums_sorted[left] == nums_sorted[left + 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


'''
解题思路：
标签：数组遍历
首先对数组进行排序，排序后固定一个数 nums[i]，再使用左右指针指向 nums[i]后面的两端，数字分别为 nums[L] 和 nums[R]，计算三个数的和sum判断是否满足为0，满足则添加进结果集
如果 nums[i]大于 0，则三数之和必然无法等于0，结束循环
如果 nums[i] == nums[i−1]，则说明该数字重复，会导致结果重复，所以应该跳过
当 sum == 0 时，nums[L] == nums[L+1] 则会导致结果重复，应该跳过，L++
当 sum == 0 时，nums[R] == nums[R−1] 则会导致结果重复，应该跳过，R--
时间复杂度：O(n^2)
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        record = set()
        nums.sort()
        if len(nums) < 3 or nums[0] > 0:
            return list(record)
        # print(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if nums[i] > 0:
                break
            while (j < k):
                if nums[i] + nums[j] > 0:
                    break
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    record.add((nums[i], nums[j], nums[k]))
                    j += 1
                else:
                    j += 1

        def getfirst(elem):
            return elem[0]

        def getsecond(elem):
            return elem[1]

        def getthird(elem):
            return elem[2]

        record = list(record)
        record.sort(key=getthird)
        record.sort(key=getsecond)
        record.sort(key=getfirst)
        return list(record)
