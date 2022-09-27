# coding:utf-8
'''
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


# 该方法用到了额外的空间，不符合题目的要求
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_1 = {}
        for each in nums:
            if each in dict_1:
                dict_1[each] += 1
            else:
                dict_1[each] = 1
        for each in dict_1.keys():
            if dict_1[each] == 1:
                return each
# 异或处理
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
'''
复杂度分析
时间复杂度：O(n)，其中 n 是数组长度。只需要对数组遍历一次。
空间复杂度：O(1)。
'''
'''
1)相等两数x, y的异或(x^y)为0
2)lambda匿名函数可以传入其的变量进行计算，
如func = lambda x,y:x+y定义了一个进行求和的匿名函数
res = func(1,2) -> res = 3
3)reduce(func, iterable)函数可对可迭代对象iterable的每一个元素
送入func进行累积运算，例如：reduce(lambda x,y:x+y, [1,2,3]) -> ((1+2)+3)=6

'''

'''
leetcode链接：
https://leetcode.cn/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
'''