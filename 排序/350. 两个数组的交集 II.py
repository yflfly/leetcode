# coding:utf-8
'''
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 数组排序
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        res = []
        index1, index2 = 0, 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
        return res


'''
讲解：
首先对两个数组进行排序，然后使用两个指针遍历两个数组。
初始时，两个指针分别指向两个数组的头部。每次比较两个指针指向的两个数组中的数字，如果两个数字不相等，则将指向较小数字的指针右移一位，当至少右一个指针超出数组范围时，遍历结束。
'''
