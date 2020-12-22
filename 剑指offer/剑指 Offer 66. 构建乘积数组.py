# coding:utf-8
'''
剑指 Offer 66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 
提示：
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
'''

# 下面的方法会超出时间限制
def constructArr(a):
    res = []
    for i in range(len(a)):
        res_1 = 1
        for j in range(len(a)):
            if i != j:
                res_1 = res_1*a[j]
        res.append(res_1)
    return res
print(constructArr([1,2,3,4,5]))

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1] # 下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1] # 上三角
            b[i] *= tmp # 下三角 * 上三角
        return b
