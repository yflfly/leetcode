# coding:utf-8
'''
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

'''


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        self.buildHeap(arr, n)
        for i in range(n - 1, -1, -1):
            self.swap(arr, i, 0)
            self.heapify(arr, i, 0)
        return arr[:k]

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def buildHeap(self, arr, n):
        for i in range((n - 2) // 2, -1, -1):
            self.heapify(arr, n, i)

    def heapify(self, arr, n, i):
        c1 = 2 * i + 1
        c2 = 2 * i + 2
        max = i
        if c1 < n and arr[c1] > arr[max]:
            max = c1
        if c2 < n and arr[c2] > arr[max]:
            max = c2
        if max != i:
            self.swap(arr, max, i)
            self.heapify(arr, n, max)
