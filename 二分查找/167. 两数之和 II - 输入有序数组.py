# coding:utf-8
'''
167. 两数之和 II - 输入有序数组
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''

'''
在数组中找到两个数，使得它们的和等于目标值，可以首先固定第一个数，
然后寻找第二个数，第二个数等于目标值减去第一个数的差。
利用数组的有序性质，可以通过二分查找的方法寻找第二个数。
为了避免重复寻找，在寻找第二个数时，只在第一个数的右侧寻找。

'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low = i + 1
            high = n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if target == numbers[mid] + numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] + numbers[i] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        return [-1, -1]


'''
# 下面的代码也能通过
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low = i + 1
            high = n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if target == numbers[mid] + numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] + numbers[i] > target:
                    high = mid - 1
                else:
                    low = mid + 1

# 题目中未规定 没有找到的返回值，所以不加返回值也是可以通过的

'''
