'''
合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小等于 m + n）来保存 nums2 中的元素。
示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

考查标签：数组、双指针
'''

# 方法一
'''
不建议这么做，面试官遇到这样的答案会直接pass掉
'''


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(len(nums2)):
            nums1[i + m] = nums2[i]
        nums1 = nums1.sort()


# 方法二：双指针
'''
一般而言，对于有序数组可以通过 双指针法 达到O(n + m)的时间复杂度。
最直接的算法实现是将指针p1 置为 nums1的开头， p2为 nums2的开头，在每一步将最小值放入输出数组中。

由于 nums1 是用于输出的数组，需要将nums1中的前m个元素放在其他地方，也就需要 O(m) 的空间复杂度。
'''


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        nums1[:] = []  # 清空list 此处需要多多注意 不能写成 nums1= [] 提交不通过
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p2 < n:
            for each in nums2[p2:]:
                nums1.append(each)
        if p1 < m:
            for each in nums1_copy[p1:]:
                nums1.append(each)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
nums1_copy = nums1[:m]
nums1[:] = []
p1, p2 = 0, 0
while p1 < m and p2 < n:
    if nums1_copy[p1] < nums2[p2]:
        nums1.append(nums1_copy[p1])
        p1 += 1
    else:
        nums1.append(nums2[p2])
        p2 += 1
if p1 < m:
    for each in nums1_copy[p1:]:
        nums1.append(each)
if p2 < n:
    for each in nums2[p2:]:
        nums1.append(each)
print(nums1)
