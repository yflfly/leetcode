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
        if len(nums1) > len(nums2):  # 假定第一个序列的长度总不大于第二个
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


# 归并排序（复杂度不满足题目要求）
'''
若题目没有要求时间复杂度，对于两个有序数组，我们很容易想到用双指针归并的思想解决，此时复杂度为O(m+n)，代码如下：
利用双指针一次比较nums1和nums2中的每个元素，当其中一个数组遍历完成后我们将另一个数组的剩余部分直接加到新数组后面即可。
这样，两个有序的数组就被我们合并成了一个有序的数组，对于一个有序的数组，我们求其中位数很简单，只需区分奇偶情况即可。
'''


class Solution:
    # o(m+n)解法
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        res = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i == m:
            res += nums2[j:n]
        if j == n:
            res += nums1[i:m]
        if len(res) % 2 == 1:  # 排序之后的数组为奇数，直接返回中间的数即可
            return res[len(res) // 2]
        else:  # 偶数，则返回中间两个数的均值
            return (res[len(res) // 2] + res[len(res) // 2 - 1]) / 2


# 二分
'''
题目要求在O(log(m+n))复杂度下完成，看到log级，且有序数组，此时我们应该考虑二分法查找其中的一个数组。代码如下:
'''


def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)
    # 交换顺序，使得m总是指向最短的那个数组
    if m > n:
        nums1, m, nums2, n = nums2, n, nums1, m
    if n == 0:
        raise ValueError
    '''
        我们来考虑一个已合并的数组，求其中位数，显然有2种情况：
        1.数组长度为奇数，中位数就等于中间的那个元素
        2.数组长度为偶数，中位数等于中间两个数之和除以2
        所以，我们在这里定义half_pos，值为m+n+1，
        由于//2为向下取整，所以这样可以将奇偶两种情况合并。
    '''
    l, r, half_pos = 0, m, (m + n + 1) // 2
    while l <= r:
        # 在m中二分查找
        i = l + (r - l) // 2
        # 因为m中取了i，所以j中只需对half_pos - i的位置进行考虑即可
        j = half_pos - i
        '''
        我们将两个数组分为2个部分，分别为左半部分[0:i] + [0:j] 与 右半部分[i:] + [j:],
        显然这符合中位数的定义，将数组分为左右元素个数相等的两部分
        在次数我们定义的i，j在偶数情况下，左右两半部分数量相等，
        奇数情况下，左半部分比右半部分多出一个元素
        '''
        # i不在左边界，因为nums1为排序数组，显然nums1[i-1] < nums1[i],所以无需比较
        # 若nums1[i-1]>nums2[j]，显然此时的i取得大了
        # 所以利用二分搜索i的左半区间
        if i > 0 and nums1[i - 1] > nums2[j]:
            r = i - 1
        # 同上
        elif i < m and nums1[i] < nums2[j - 1]:
            l = i + 1
        else:
            # i取到了nums1的左边界，此时nums1的左边没有元素了，显然此时左半部分的最大值是nums2[j-1]
            if i == 0:
                max_of_left = nums2[j - 1]
            # 同上
            elif j == 0:
                max_of_left = nums1[i - 1]
            # i，j均不为0，此时，i，j都取在了中间的位置，那么左半部分最大值为max(nums1[i-1], nums2[j-1])
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])
            # 若该数组长度为奇数，直接返回max_of_left即可
            if (m + n) % 2 == 1:
                return max_of_left
            # 若该数组长度为偶数，则同上找出右半部分的最小值
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            # 返回两个数之和的一半
            return (max_of_left + min_of_right) / 2.0
