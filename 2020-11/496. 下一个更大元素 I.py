# coding:utf-8
'''
496. 下一个更大元素 I

给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
 

提示：
nums1和nums2中所有元素是唯一的。
nums1和nums2 的数组大小都不超过1000。
'''

# 下面是本人的方法
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for each in nums1:
            if each == nums2[-1]:
                res.append(-1)
                continue
            tag = 0
            for i in range(nums2.index(each) + 1, len(nums2)):
                if nums2[i] > each:
                    tag += 1
                    res.append(nums2[i])
                    break
            if tag == 0:
                res.append(-1)
        return res

'''
# 别人的方法
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        方法一：先找到该元素在nums2中的位置，然后再找它之后比它大的
        时间复杂度：O(n2)
        """
        # res = []
        # for i in nums1:
        #     flag = 0
        #     bigger = -1
        #     for j in nums2:
        #         if i == j:
        #             flag = 1
        #         if flag == 1 and i < j:
        #             bigger = j
        #             break;
        #     res.append(bigger)
        # return res
        """
        方法二：从后往前找，遇到比它大的就更新，直到遇到它
        时间复杂度：O(n2)
        """
        # res = []
        # for i in nums1:
        #     bigger = -1
        #     for j in range(1,len(nums2)):
        #         if nums2[-j] == i:
        #             break
        #         if nums2[-j] > i:
        #             bigger = nums2[-j]
        #     res.append(bigger)
        # return res
        """
        方法三：为nums2维护一个字典，key为当前元素，value为该元素的下一个比其大的值
        设置一个递减栈，当遇到更大的元素时，把栈里比他小的元素都放到字典中
        查找时只需要在字典中找。时间复杂度O(n+m) 空间复杂度O(m)
        """
        hash_dict = dict()
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                hash_dict[stack.pop()] = i
            stack.append(i)
        return [hash_dict.get(i,-1) for i in nums1]
'''