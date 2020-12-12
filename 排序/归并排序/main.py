# coding:utf-8
import time


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left_num = nums[: middle]
    right_num = nums[middle:]
    return merge(merge_sort(left_num), merge_sort(right_num))


def merge(left_num, right_num):
    len_left = len(left_num)
    len_right = len(right_num)
    i = j = 0
    result = []
    while i < len_left and j < len_right:
        if left_num[i] > right_num[j]:
            result.append(right_num[j])
            j += 1
        else:
            result.append(left_num[i])
            i += 1
    if i == len_left and j < len_right:
        for m in right_num[j:]:
            result.append(m)
    if j == len_right and i < len_left:
        for m in left_num[i:]:
            result.append(m)
    return result


if __name__ == "__main__":
    start = time.time()
    #    for i in range(1000):
    a = [4, 2, 4, 5, 7, 8, 12, 23, 1]
    result = merge_sort(a)
    end = time.time()
    print(result)
    print('Running time: %s Seconds' % (end - start))

'''
归并排序参考网址：
https://zhuanlan.zhihu.com/p/124356219
'''