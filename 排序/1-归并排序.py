# coding:utf-8
'''
拆分到单个元素，然后两个两个往上进行递归合并。设置left 和right两个游标,进行合并。
时间复杂度：o(nlogn)
'''


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


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left_num = nums[: middle]
    right_num = nums[middle:]
    return merge(merge_sort(left_num), merge_sort(right_num))


if __name__ == "__main__":
    a = [4, 2, 4, 5, 7, 8, 12, 23, 1]
    result = merge_sort(a)
    print(result) # [1, 2, 4, 4, 5, 7, 8, 12, 23]



'''
归并排序，是创建再归并操作上的一种有效的排序算法
算法采用分治法的一个非常典型的应用，且各层分治递归可以同时进行
归并排序思路简单，速度仅次于快速排序，为问丁排序算法，一般用于对总体无序，但是各子项相对有序的序列
'''

'''
归并排序参考网址：
https://zhuanlan.zhihu.com/p/124356219

归并排序是用分治思想，分治模式在每一层递归上有三个步骤：
分解（Divide）：将n个元素分成个含n/2个元素的子序列。
解决（Conquer）：用合并排序法对两个子序列递归的排序。
合并（Combine）：合并两个已排序的子序列已得到排序结果。

'''
