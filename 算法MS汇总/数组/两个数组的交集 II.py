'''
两个数组的交集 II
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。

考查标签 排序、哈希表、双指针、二分查找
'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        index1 = 0
        index2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        nums1.sort()
        nums2.sort()
        while index1 < len1 and index2 < len2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                res.append(nums1[index1])
                index1 += 1
                index2 += 1
        return res
