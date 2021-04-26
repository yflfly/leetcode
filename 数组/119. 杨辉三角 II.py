'''
119. 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 3
输出: [1,3,3,1]
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            tmp = []
            for j in range(i + 1):
                if j == 0:
                    tmp.append(1)
                elif j == i:
                    tmp.append(1)
                else:
                    tmp.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(tmp)
        return res[-1]
