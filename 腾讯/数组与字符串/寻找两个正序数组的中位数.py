'''
寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000

考查点标签：数组、二分查找、分治算法
'''


# 方法一：一般的方法，但是时间复杂度不符合题目的要求
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = []
        for each in nums1:
            list1.append(each)
        for each in nums2:
            list1.append(each)
        list1.sort()
        if len(list1) % 2 == 0:
            middle = len(list1) // 2
            return float(list1[middle - 1] + list1[middle]) / 2.0
        else:
            middle = len(list1) // 2
            return float(list1[middle])


'''
题目中要求时间复杂度为log(m+n)，log的时间复杂度一般是使用二分查找来做
'''


# 方法二：二分查找
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  # 假定第一个学列的长度总不大于第二个
            nums1, nums2 = nums2, nums1
        # 记录两个序列的长度
        len1, len2 = len(nums1), len(nums2)
        left, right, half_len = 0, len1, (len1 + len2 + 1) // 2
        mid1 = (left + right) // 2
        mid2 = half_len - mid1

        while left < right:
            if mid1 < len1 and nums2[mid2 - 1] > nums1[mid1]:
                left = mid1 + 1
            else:
                right = mid1
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

        if mid1 == 0:
            max_of_left = nums2[mid2 - 1]
        elif mid2 == 0:
            max_of_left = nums1[mid1 - 1]
        else:
            max_of_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

        if (len1 + len2) % 2 == 1:
            return max_of_left

        if mid1 == len1:
            min_of_right = nums2[mid2]
        elif mid2 == len2:
            min_of_right = nums1[mid1]
        else:
            min_of_right = min(nums1[mid1], nums2[mid2])

        return (max_of_left + min_of_right) / 2

