'''
螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

考查标签：数组
'''

'''
按照正常的逻辑顺序继续遍历矩阵就好
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1
            if right < left:
                break
            for k in range(right, left - 1, -1):
                res.append(matrix[bottom][k])
            bottom -= 1
            if bottom < top:
                break
            for l in range(bottom, top - 1, -1):
                res.append(matrix[l][left])
            left += 1
            if left > right:
                break
        return res
