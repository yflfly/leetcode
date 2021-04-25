'''
面试题 16.21. 交换和
给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。
若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。
示例:
输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
输出: [1, 3]
示例:
输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
输出: []
'''


# 会超时
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1 = sum(array1)
        sum2 = sum(array2)
        for i in range(len(array1)):
            for j in range(len(array2)):
                if sum1 - array1[i] + array2[j] == sum2 + array1[i] - array2[j]:
                    return [array1[i], array2[j]]
        return []

class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        if not array1 or not array2:
            return []
        sum1 = sum(array1)
        sum2 = sum(array2)
        # 两个数组的差为奇数，说明一定没法平分达到相等
        diff = sum1-sum2
        if diff % 2 != 0:
            return []
        # 对需要查询元素是否存在的数组，进行去重，提升查询效率，避免超时
        array2 = set(array2)
        for item in array1:
            if (item - diff // 2) in array2:
                return [item, item - diff // 2]

        return []
