'''
1854. 人口最多的年份
给你一个二维整数数组 logs ，其中每个 logs[i] = [birthi, deathi] 表示第 i 个人的出生和死亡年份。
年份 x 的 人口 定义为这一年期间活着的人的数目。第 i 个人被计入年份 x 的人口需要满足：x 在闭区间 [birthi, deathi - 1] 内。注意，人不应当计入他们死亡当年的人口中。
返回 人口最多 且 最早 的年份。
示例 1：
输入：logs = [[1993,1999],[2000,2010]]
输出：1993
解释：人口最多为 1 ，而 1993 是人口为 1 的最早年份。
示例 2：
输入：logs = [[1950,1961],[1960,1971],[1970,1981]]
输出：1960
解释：
人口最多为 2 ，分别出现在 1960 和 1970 。
其中最早年份是 1960 。
'''


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta = [0] * 101  # 变化量
        offset = 1950  # 起始年份与起始下标之差
        for b, d in logs:
            delta[b - offset] += 1
            delta[d - offset] -= 1
        mx = 0  # 人口数量最大值
        res = 0  # 最大值对应的最小下标
        curr = 0  # 每一年的人口数量
        # 前缀和
        for i in range(101):
            curr += delta[i]
            if curr > mx:
                mx = curr
                res = i
        return res + offset  # 转回对应的年份
