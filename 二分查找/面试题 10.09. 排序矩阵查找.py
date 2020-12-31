# coding:utf-8
'''
面试题 10.09. 排序矩阵查找
给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''

'''
因为数组是每一行、每一列都按升序排列，可以从最后一行开始，若一行的第一个数字大于target，则整行都是大于target的，则跳到上一行继续查找
当一行不大于target，则将整行放入二分查找的函数中，进行查找
具体的代码如下所示：
'''

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                return True
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for i in range(-1, -len(matrix) - 1, -1):
            if matrix[i][0] > target:
                continue
            if self.search(matrix[i], target):
                return True
        return False



# 下面的方法也可以通过，知道就可以，但是尽量不要这么做
'''
import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = np.array(matrix)
        if target in matrix:
            return True
        return False
'''
