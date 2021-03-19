# coding:utf-8
'''
指定第一个数为mid_value,排序使得mid_value左边的数比mid_value小，右边的数比mid_value大，然后分别对左边和右边进行递归排序。
时间复杂度：o(nlogn)
'''

def quick_sort(alist, start, end):
    if start >= end:
        return

    mid_value = alist[start]
    low = start
    high = end

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] <= mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    quick_sort(li, 0, len(li) - 1)
    print(li)  # [13, 17, 20, 26, 31, 44, 54, 55, 77, 93]
