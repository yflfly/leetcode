'''
229. 求众数 II
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
示例 1：
输入：[3,2,3]
输出：[3]
示例 2：
输入：nums = [1]
输出：[1]
示例 3：
输入：[1,1,1,3,3,2,2,2]
输出：[1,2]
'''


# 空间复杂度不符合题目的要求
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1 = {}
        for each in nums:
            if each in dict1:
                dict1[each] += 1
            else:
                dict1[each] = 1
        count = len(nums) // 3
        res = []
        for key in dict1:
            if dict1[key] > count:
                res.append(key)
        return res


# 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a, b, count_a, count_b = 0, 0, 0, 0  # 设定1号众数和2号众数
        res = []

        for i in nums:
            if a == i:  # 频数统计的优先顺序要大于频数为0的判断
                count_a += 1
                continue
            if b == i:
                count_b += 1
                continue
            if count_a == 0:
                a = i
                count_a = 1
                continue
            if count_b == 0:
                b = i
                count_b = 1
                continue
            count_a -= 1
            count_b -= 1

        count_a, count_b = 0, 0  # 重置计数器
        for j in nums:  # 再检验
            if j == a:
                count_a += 1
            elif j == b:
                count_b += 1
        if count_a > len(nums) / 3:
            res.append(a)
        if count_b > len(nums) / 3:
            res.append(b)
        return res
'''
复杂度分析
时间复杂度：O(N)
空间复杂度：O(1)
'''

'''
如果至多选一个代表，那他的票数至少要超过一半（⌊ 1/2 ⌋）的票数；
如果至多选两个代表，那他们的票数至少要超过 ⌊ 1/3 ⌋ 的票数；
如果至多选m个代表，那他们的票数至少要超过 ⌊ 1/(m+1) ⌋ 的票数。
所以以后碰到这样的问题，而且要求达到线性的时间复杂度以及常量级的空间复杂度，直接套上摩尔投票法。
'''