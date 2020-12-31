'''
面试题 01.08. 零矩阵
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
示例 1：
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：
输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
'''
'''
两次遍历：
第一次遍历，用两个数组记录哪一行或者哪一列有0。
第二次遍历，若行i或列j有个元素为0，则将当前元素置0.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, column = len(matrix) * [0], len(matrix[0]) * [0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    column[j] = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == 1 or column[j] == 1:
                    matrix[i][j] = 0


