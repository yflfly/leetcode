'''
面试题 16.06. 最小差
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出： 3，即数值对(11, 8)
提示：

1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间[-2147483648, 2147483647]内

'''


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        res = float('inf')
        n = len(a)
        m = len(b)
        i, j = 0, 0
        while i < n and j < m:
            if a[i] > b[j]:
                res = min(res, a[i] - b[j])
                j += 1
            elif a[i] < b[j]:
                res = min(res, b[j] - a[i])
                i += 1
            else:
                return 0
        return res
'''
相关类型的题目：
https://leetcode-cn.com/problems/smallest-difference-lcci/solution/wo-shi-ni-de-ma-ma-ya-di-yi-qi-by-fe-lucifer/
'''
