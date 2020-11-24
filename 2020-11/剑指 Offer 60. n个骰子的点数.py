# coding:utf-8
'''
剑指 Offer 60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例 2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
 
限制：
1 <= n <= 11
通过次数27,925提交次数51,514

'''


class Solution:
    def twoSum(self, n: int) -> List[float]:
        remember = {(1, 1): 1, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1, (1, 6): 1}

        def getCount(n, k):
            nonlocal remember
            res = 0
            if (n, k) in remember:
                return remember[(n, k)]
            for i in range(k - 6, k):
                if i >= n - 1 and i <= 6 * (n - 1):
                    res += getCount(n - 1, i)
            remember[(n, k)] = res
            return res

        res = [0] * (5 * n + 1)
        for i in range(len(res)):
            res[i] = getCount(n, i + n)  # i+n是为了索引与理论上的k值对齐
        s = sum(res)
        return [i / s for i in res]