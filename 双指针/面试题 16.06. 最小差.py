'''
面试题 16.06. 最小差
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差
示例：
输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出：3，即数值对(11, 8)

考查标签 双指针
'''


# 方法一：会出现超时地问题
class Solution:
    def smallestDifference(self, a, b) -> int:
        a.sort()
        b.sort()
        min_1 = abs(a[0] - b[0])
        for i in range(len(a)):
            for j in range(len(b)):
                abs_res = abs(a[i] - b[j])
                if abs_res > min_1:
                    continue
                else:
                    min_1 = abs_res
        return min_1


A = Solution()
a = [1, 3, 15, 11, 2]
b = [23, 127, 235, 19, 8]

a = [1, 2, 11, 15]
b = [4, 12, 19, 23, 127, 235]
print(A.smallestDifference(a, b))

# 方法二：排序+双指针
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        # 先排序，便于双指针遍历
        a.sort()
        b.sort()
        res = float('inf')
        n = len(a)
        m = len(b)
        # 双指针
        i, j = 0, 0
        while i < n and j < m:
            # 将小的数的指针前进一步，这样才可能让差值更小
            if a[i] > b[j]:
                res = min(res, a[i] - b[j])
                j += 1
            elif a[i] < b[j]:
                res = min(res, b[j] - a[i])
                i += 1
            else:
                return 0
        return res
