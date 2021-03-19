# coding:utf-8

def bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        if 0 == count:
            break
    return alist
lst = [3, 5, 1, 2, 4, 10]
print(bubble_sort(lst))  # [1, 2, 3, 4, 5, 10]

'''
每一趟选出一个最大值，排在最后一个
时间复杂度：o(n^2)
'''