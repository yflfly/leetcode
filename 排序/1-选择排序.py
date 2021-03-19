# coding:utf-8
'''
每一趟选出一个最小值，放到前面
时间复杂度：o(n^2)
'''


def select_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


lst = [3, 5, 1, 2, 4, 10]
print(select_sort(lst))  # [1, 2, 3, 4, 5, 10]
