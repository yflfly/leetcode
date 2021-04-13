'''
523. 连续的子数组和
给定一个包含 非负数 的数组和一个目标 整数 k ，编写一个函数来判断该数组是否含有连续的子数组，
其大小至少为 2，且总和为 k 的倍数，即总和为 n * k ，其中 n 也是一个整数。
示例 1：
输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2：
输入：[23,2,6,4,7], k = 6
输出：True
解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
'''


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if k == 0:
            for index in (1, len(nums)):
                if nums[index - 1] == 0 and numsp[index] == 0:
                    return True
            return False

        dic = {0: -1}
        now = nums[0] % k
        if now not in dic:
            dic[now] = 0
        for i in range(1, len(nums)):
            now += nums[i]
            now = now % k
            if now in dic:
                if i - dic[now] >= 2:
                    return True
            else:
                dic[now] = i
        return False
'''
讲解参考网址：
https://zhuanlan.zhihu.com/p/261032244
'''
