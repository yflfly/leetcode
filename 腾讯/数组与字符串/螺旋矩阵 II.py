'''
螺旋矩阵 II
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        num = 1
        tar = n * n
        res = [[0 for i in range(n)] for j in range(n)]
        while num <= tar:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1
            for j in range(top, bottom + 1):
                res[j][right] = num
                num += 1
            right -= 1
            for k in range(right, left - 1, -1):
                res[bottom][k] = num
                num += 1
            bottom -= 1
            for m in range(bottom, top - 1, -1):
                res[m][left] = num
                num += 1
            left += 1
        return res
