# coding:utf-8
'''
剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"
 
提示:
0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
'''


# 下面是有问题的代码，要仔细审题目
def minNumber(nums):
    linshi = []
    for each in nums:
        linshi.extend([int(each) for each in list(str(each))])
    linshi.sort()
    print(linshi)
    str1 = ''
    str2 = ''
    for each in linshi:
        if each == 0:
            str2 = str2 + str(0)
        elif str1 == '':
            str1 = str(each) + str2
        else:
            str1 = str1 + str(each)
    return str1


print(minNumber([3, 30, 34, 5, 9]))
