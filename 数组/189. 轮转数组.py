'''
189. 轮转数组
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。
进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为O(1) 的原地算法解决这个问题吗？
示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

考查标签：数组
'''


# 该方法需要重新申请一个空间
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums
        k = len(nums) % k
        res = []
        for each in nums[-k:]:
            res.append(each)
        for each in nums[:len(nums) - k]:
            res.append(each)
        return res


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            x = nums.pop()
            nums.insert(0, x)

'''
可以根据结果，换种思路。
先全部反转，将元素提到最前面
反转前半部分
反转后半部分
然后返回结果
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return

        n = len(nums)
        k %= n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k := (k % len(nums)):
            nums[:k], nums[k:] = nums[-k:], nums[:-k]
'''