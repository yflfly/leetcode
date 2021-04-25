'''
面试题 17.14. 最小K个数
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
示例：
输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
'''


# 利用python自带的排序算法
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        arr.sort()
        return arr[:k]


# 实现快速排序
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        def fast(arr, start, end):
            if start >= end:
                return
            low = start
            high = end
            mid_val = arr[low]
            while low < high:
                while low < high and arr[high] >= mid_val:
                    high -= 1
                arr[low] = arr[high]
                while low < high and arr[low] < mid_val:
                    low += 1
                arr[high] = arr[low]
            arr[low] = mid_val
            fast(arr, start, low-1)
            fast(arr, low + 1, end)

        fast(arr, 0, len(arr) - 1)
        return arr[:k]
