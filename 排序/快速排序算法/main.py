# coding:utf-8
import time


def quick_sort(nums, first, last):
    if first > last:
        return
    mid_val = nums[first]
    high = last
    low = first
    while low < high:
        while low < high and nums[high] >= mid_val:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < mid_val:
            low += 1
        nums[high] = nums[low]

    nums[low] = mid_val
    quick_sort(nums, first, low - 1)
    quick_sort(nums, low + 1, last)


if __name__ == "__main__":
    start = time.time()
    #    for i in range(1000):
    a = [4, 2, 4, 5, 7, 8, 12, 23, 1]
    quick_sort(a, 0, len(a) - 1)
    end = time.time()
    print(a)
    print('Running time: %s Seconds' % (end - start))
