# coding:utf-8
import time

'''
快速排序的思想：通过一趟排序将待排记录分隔成独立的两个部分，其中一部分记录的关键字均比另一部分的关键字小，
则可分别对这两部分记录继续进行排序，以达到整个序列有序
'''


def quick_sort(nums, first, last):
    if first > last:
        return
    mid_val = nums[first]  # 基准  先在low处挖一个坑，从后面开始找数字补坑，再挖坑
    high = last
    low = first
    while low < high:
        while low < high and nums[high] >= mid_val:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < mid_val:
            low += 1
        nums[high] = nums[low]
        print(nums)

    nums[low] = mid_val  # 外层while循环的结束条件 就是 low==high 所以此处的low也可以是high
    quick_sort(nums, first, low - 1)
    quick_sort(nums, low + 1, last)


if __name__ == "__main__":
    start = time.time()
    #    for i in range(1000):
    a = [4, 2, 4, 5, 7, 8, 12, 23, 1]
    quick_sort(a, 0, len(a) - 1)
    end = time.time()
    # print(a)
    # print('Running time: %s Seconds' % (end - start))

'''
快速排序的讲解参考网址：
https://baijiahao.baidu.com/s?id=1667443239764190065&wfr=spider&for=pc
挖坑讲解网址：
https://www.runoob.com/w3cnote/quick-sort.html
'''
