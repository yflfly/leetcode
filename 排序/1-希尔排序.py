# coding:utf-8
'''
希尔排序
是一种分组插入排序算法
时间复杂度：o(nlogn) ~ o(n^2)
'''
'''
希尔排序是插入排序的一种，是对直接插入排序算法的改进
希尔排序目的为了加快速度改进了插入排序，交换不相邻的元素对数组的局部进行排序，并最终用插入排序将局部有序的数组排序。
在此我们选择增量 gap=length/2，缩小增量以 gap = gap/2 的方式，用序列 {n/2,(n/2)/2...1} 来表示。
'''


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j > 0:
                if alist[j] < alist[j - gap]:
                    alist[j], alist[j - gap] = alist[j - gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return alist


lst = [3, 5, 1, 2, 4, 10]
print(shell_sort(lst))  # [1, 2, 3, 4, 5, 10]

'''
参考讲解网址：
https://m.runoob.com/data-structures/shell-sort.html
'''