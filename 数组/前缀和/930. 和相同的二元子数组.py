'''
930. 和相同的二元子数组
在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。
示例：
输入：A = [1,0,1,0,1], S = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1,0,1] # 前3个
[1,0,1,0,1] # 前4个
[1,0,1,0,1] # 后4个
[1,0,1,0,1] # 后3个
'''


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        dic = {0: 1}
        sum1 = 0
        res = 0
        for num in A:
            sum1 += num
            if sum1 - S in dic:
                res += dic[sum1 - S]
            if sum1 in dic:
                dic[sum1] += 1
            else:
                dic[sum1] = 1
        return res
