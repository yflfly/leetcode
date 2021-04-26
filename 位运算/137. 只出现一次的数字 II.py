'''
137. 只出现一次的数字 II
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
示例 1：
输入：nums = [2,2,3,2]
输出：3
示例 2：
输入：nums = [0,1,0,1,0,1,99]
输出：99
'''
# 方法一：HashMap
'''
遍历输入数组，统计每个数字出现的次数，最后返回出现次数为1的数字
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for key, values in dic.items():
            if values == 1:
                return key


'''
复杂度分析：
时间复杂度：O(N)，遍历输入数组。
空间复杂度：O(N)，存储N/3个元素的集合。
'''

# 方法二：位运算
'''
~x 表示 NOT
x&y 表示 AND
x
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once
