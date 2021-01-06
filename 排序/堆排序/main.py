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
    print('len_heap', len_heap)
    print('len_mid_heap', len_mid_heap)

    for i in range(len_mid_heap):
        heap_adjust(nums, len_mid_heap - i, len_heap)

    for i in range(len_heap - 1):
        swap(nums, len_heap - i, 1)
        heap_adjust(nums, 1, len_heap - i - 1)
    return list(nums)[1:]


def main():
    L = deque([50, 16, 30, 10, 60, 90, 2, 80, 70])
    print('初始', L)
    L.appendleft(0)
    print('初始', L)
    print(heap_sort(L))


if __name__ == '__main__':
    main()
'''
堆排序参考网址：
https://blog.csdn.net/sxhelijian/article/details/50295637


堆排序涉及到的概念：
1、堆排序是利用 堆进行排序的
2、堆是一种完全二叉树
3、堆有两种类型: 大根堆 小根堆
4、两种类型的概念如下：
    1）大根堆：每个结点的值都大于或等于左右孩子结点
    2）小根堆：每个结点的值都小于或等于左右孩子结点

完全二叉树：是一种除了最后一层之外的其他每一层都被完全填充，并且所有结点都保持向左对齐的树
'''
