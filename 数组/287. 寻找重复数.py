'''
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
示例 1：
输入：nums = [1,3,4,2,2]
输出：2
示例 2：
输入：nums = [3,1,3,4,2]
输出：3
示例 3：
输入：nums = [1,1]
输出：1
示例 4：
输入：nums = [1,1,2]
输出：1
'''


# 方法一：哈希表
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for each in nums:
            if each in dic:
                return each
            else:
                dic[each] = 1


# 方法二：快慢指针
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                fast = 0
                while nums[slow] != nums[fast]:
                    slow = nums[slow]
                    fast = nums[fast]
                return nums[slow]


'''
复杂度分析：
时间复杂度：O(n)
空间复杂度：O(1)
'''
