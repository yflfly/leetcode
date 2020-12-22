# coding:utf-8
'''

9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''


def isPalindrom(x):
    if x < 0:
        return False
    list1 = list(str(x))
    list2 = [each for each in list1]
    list1.reverse()
    if list1 == list2:
        return True
    else:
        return False


print(isPalindrom(121))