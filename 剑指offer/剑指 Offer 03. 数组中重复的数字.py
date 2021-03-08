'''
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
'''

'''
方法一：哈希表/字典
初始化：创建一个空字典
遍历数组nums的每一个元素，当元素不在字典中，则放入字典，否则说明元素重复，直接返回

复杂度分析：
时间复杂度O(N)：遍历数组使用O(N)，字典元素的添加与查找元素皆为O(1)
空间复杂度O(N)：字典存储元素占用O(N)大小的额外空间
'''


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dict1 = {}  # 创建一个空字典
        for each in nums:  # 遍历数组nums
            if each not in dict1:  # 若元素第一次出现，则放入字典
                dict1[each] = 1
            else:  # 若元素不只一次出现，则返回该元素
                return each
        return -1  # 本题中一定有重复数字，因此这里返回多少都可以


'''
方法二：原地交换
仔细审题，题目中“在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内”，即数组元素的索引和值是一对多的关系
因此，可遍历数组并通过交换操作，使元素的索引与值一一对应，通过索引映射对应的值，起到与字典等价的作用

例子：
     索引     0   1   2   3   4   5   6
       值     2   3   1   0   2   5   3
第一次交换     1   3   2   0   2   5   3   交换0、2
第二次交换     3   1   2   0   2   5   3   交换0、1
第三次交换     0   1   2   3   2   5   3   交换0、3
不进行交换     0   1   2   3   2   5   3   此时遍历到4位置的2，与2位置的2重复，则返回重复的数字2

'''


class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
