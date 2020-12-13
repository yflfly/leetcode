# coding:utf-8
from collections import deque


def heap_adjust(nums, start, end):
    temp = nums[start]
    i = start
    j = start * 2

    while j <= end:
        if j < end and nums[j] < nums[j + 1]:
            j += 1
        if temp < nums[j]:
            nums[i] = nums[j]
            i = j
            j = i * 2
        else:
            break
    nums[i] = temp


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]
    return nums


def heap_sort(nums):
    len_heap = len(nums) - 1
    len_mid_heap = int(len_heap / 2)

    for i in range(len_mid_heap):
        heap_adjust(nums, len_mid_heap - i, len_heap)

    for i in range(len_heap - 1):
        swap(nums, len_heap - i, 1)
        heap_adjust(nums, 1, len_heap - i - 1)
    return list(nums)[1:]


def main():
    L = deque([50, 16, 30, 10, 60, 90, 2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))


if __name__ == '__main__':
    main()
