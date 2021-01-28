'''
1539. 第 k 个缺失的正整数
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
请你找到这个数组里第 k 个缺失的正整数。
示例 1：
输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
示例 2：
输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
 
考查标签 哈希表
'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = [i for i in range(arr[-1] + k + 1)]
        for each in arr:
            missing[each] = 0
        for j in range(1, len(missing)):
            if missing[j] != 0:
                k -= 1
            if k == 0:
                return missing[j]

'''
建立一个missing数组记录1到arr[-1]+k的值，首位补零，这样使得索引值就等于元素值，遍历arr，
凡是arr中出现过的元素，missing中设置为0，最后遍历missing，找出缺失的第k个值。

代码讲解网址：
https://leetcode-cn.com/problems/kth-missing-positive-number/solution/ji-yi-hua-by-yi-wen-statistics/
'''