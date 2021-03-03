# coding:utf-8
'''
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2]
输出：1
示例 2：
输入：[2,2,2,0,1]
输出：0

'''


# 方法一：二分法
'''
因为题目中指定排序数组，所以第一想法就是可不可以用二分法进行解决
我们要找的最小值其实是右排序数组的第一个数据

具体的做法流程如下所示：
用i,j指向数组头和尾，中间点m=（i+j）/2。
当num[m]>num[j]时，m一定在左侧数组中，我们要找的区间在[m+1,j]
当num[m]<num[j]时，m一定在右侧数组中，我们要找的区间在[i，m]
当num[m]=num[j]时，无法判断在在哪个数组中，我们只能j=j-1缩小范围找。
举个例子：
[1,0,1,1,1] ，我们要找的在区间在左侧
[1,1,1,0,1]，而此时要找的区间在右侧
'''
class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]
'''
讲解参考网址：
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-by-leetcode-s/
'''

# 方法二：直接遍历数组，找到非递增位置返回就行，但是这样的做法运行时间太长
class Solution:
    def minArray(self, numbers: [int]) -> int:
        num = numbers[0]
        for i in range(1, len(numbers)):
            if num <= numbers[i]:
                num = numbers[i]
                continue
            else:
                return numbers[i]
        return numbers[0]
