# coding:utf-8
'''
560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
'''


# 下面的方法在提交的过程中会出现超时间限制
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum(nums[i:j]) == k:
                    res.append(nums[i:j])
        return len(res)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0: 1}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if ((sum - k) in hash):
                count += hash[sum - k]
            if (sum in hash):
                hash[sum] += 1
            else:
                hash[sum] = 1
        return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = 0  # 前缀和
        ans = 0
        dp = dict()  # 存放 前缀和:出现次数，键值对，初始化一个0:1，为了考虑到从头开始到某点的子数组正好为答案。
        dp[0] = 1
        for i in range(n):
            pre += nums[i]  # 计算前缀和
            if pre - k in dp:  # 如果pre-k这个前缀存在，那么答案加上它出现的次数
                ans += dp[pre - k]
            if pre in dp:  # 更新dp[pre]
                dp[pre] += 1
            else:
                dp[pre] = 1
        return ans


'''
参考讲解：
https://zhuanlan.zhihu.com/p/135908437
'''
'''
讲解网址：
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/ha-xi-biao-zhu-xing-jie-shi-python3-by-zhu_shi_fu/
'''
