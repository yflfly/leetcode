# coding:utf-8
'''
1491. 去掉最低工资和最高工资后的工资平均值
给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。
请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。
示例 1：
输入：salary = [4000,3000,1000,2000]
输出：2500.00000
解释：最低工资和最高工资分别是 1000 和 4000 。
去掉最低工资和最高工资以后的平均工资是 (2000+3000)/2= 2500
示例 2：
输入：salary = [1000,2000,3000]
输出：2000.00000
解释：最低工资和最高工资分别是 1000 和 3000 。
去掉最低工资和最高工资以后的平均工资是 (2000)/1= 2000
示例 3：
输入：salary = [6000,5000,4000,3000,2000,1000]
输出：3500.00000
示例 4：
输入：salary = [8000,9000,2000,3000,6000,1000]
输出：4750.00000
 
提示：
3 <= salary.length <= 100
10^3 <= salary[i] <= 10^6
salary[i] 是唯一的。
与真实值误差在 10^-5 以内的结果都将视为正确答案。

'''


# 未使用排序的方法
class Solution:
    def average(self, salary: List[int]) -> float:
        max_ = max(salary)
        min_ = min(salary)
        sum_ = sum(salary) - max_ - min_
        return float(sum_) / (len(salary) - 2)
'''
复杂度
时间复杂度：O(n)。选取最大值、最小值和求和的过程的时间代价都是 O(n)，故渐进时间复杂度为 O(n)。
空间复杂度：O(1)。这里只用到了常量级别的辅助空间。
'''

# 排序 移除最大值和最小值，然后求平均
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop()
        return mean(salary)