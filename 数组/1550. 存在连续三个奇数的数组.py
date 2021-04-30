'''
1550. 存在连续三个奇数的数组
给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。
示例 1：
输入：arr = [2,6,4,1]
输出：false
解释：不存在连续三个元素都是奇数的情况。
示例 2：
输入：arr = [1,2,34,3,4,5,7,23,12]
输出：true
解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。
'''


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        dp = [0 for _ in arr]
        dp[0] = 1 if arr[1] % 2 != 0 else 0
        for i in range(1, len(arr)):
            if arr[i] % 2 != 0:
                dp[i] = dp[i - 1] + 1
                if dp[i] == 3:
                    return True
        return False
