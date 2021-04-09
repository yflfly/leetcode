'''
923. 三数之和的多种可能
给定一个整数数组A，以及一个整数target作为目标值，返回满足i < j < k且A[i] + A[j] + A[k] == target 的元组 i, j, k 的数量。
由于结果会非常大，请返回 结果除以 10^9 + 7 的余数。
示例 1：
输入：A = [1,1,2,2,3,3,4,4,5,5], target = 8
输出：20
解释：
按值枚举（A[i]，A[j]，A[k]）：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
示例 2：
输入：A = [1,1,2,2,2,2], target = 5
输出：12
解释：
A[i] = 1，A[j] = A[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
'''
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(A)
        A.sort()
        first_idx, last_idx = {}, {}
        for i, num in enumerate(A):
            if num not in first_idx:
                first_idx[num] = i
            last_idx[num] = i  # 记录排序后，0-9最后出现的位置
        ans = 0

        for first in range(n - 2):  # 枚举第一个元素
            second, third = first + 1, n - 1
            two_target = target - A[first]
            while second < third:
                s = A[second] + A[third]
                if s > two_target:  # 当前数值太大
                    third -= 1
                elif s < two_target:  # 当前数值太小
                    second += 1
                else:  # 遇到一个组合能够满足了
                    if A[second] == A[third]:
                        num_second = last_idx[A[third]] - max(second, first) + 1
                        ans += num_second * (num_second-1) // 2 # 这个组合的数量
                        break                                   # 直接枚举第二个first
                    else:
                        num_second = last_idx[A[second]] - max(second, first) + 1
                        num_third = third - first_idx[A[third]] + 1
                        ans = ans + num_second * num_third  # 这个组合的数量
                        third = first_idx[A[third]] - 1     # 重新赋值
                        second = last_idx[A[second]] + 1
        ans %= MOD
        return ans
