'''
1248. 统计「优美子数组」
给你一个整数数组 nums 和一个整数 k。
如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
请返回这个数组中「优美子数组」的数目。
示例 1：
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：
输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：
输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
'''
'''
本题两大关键特征：
1）连续子数组
2）子数组内恰好有k个奇数数字
'''


# 方法：前缀和

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 因为只是找奇数的个数，与数组的值大小无关，将所有奇数记为1，偶数记为0
        # 题目变为 “找和为K的子数组”
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0

        # 前缀和 + 哈希字典
        res = 0
        summ = 0
        dic = {}
        dic[0] = 1  # 当出现summ-k==0时，res需要+1
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in dic.keys():
                res += dic[summ - k]
            if summ not in dic.keys():
                dic[summ] = 1
            else:
                dic[summ] += 1
        return res


'''
https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/de-liao-wo-ba-qian-zhui-he-gei-ba-de-gan-ymzz/
'''
