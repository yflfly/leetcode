'''
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
'''
'''
首先选取数组中右上角的数字，
如果该数字等于要查找的数字，查找过程结束；
如果该数字大于要查找的数字，剔除这个数字所在的列；
如果该数字小于要查找的数字，剔除这个数字所在的行
也就是说，如果要查找的数字不在数组的右上角，则每一次都在数组的查找范围中剔除一行或者一列，这样每一步都可以缩小查找范围，直到找到要查找的数字，或者查找范围为空
'''

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        column = len(matrix[0]) - 1
        line = 0
        while line < len(matrix):
            while column >= 0:
                if matrix[line][column] > target:
                    column -= 1
                elif matrix[line][column] == target:
                    return True
                else:
                    break
            line = line + 1
        return False
