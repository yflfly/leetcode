'''
1004. 最大连续1的个数 III
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。
示例 1：
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：
输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
'''


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zero = 0
        max_len = 0
        n = len(A)
        right = 0
        left = 0
        while right < n:
            if A[right] == 0:
                zero += 1
            while zero >K:
                if A[left] == 0:
                    zero -= 1
                left += 1
            max_len = max(max_len,right-left+1)
            right += 1
        return max_len
'''
复杂度分析：
时间复杂度：O(N)，因为每个元素只遍历了一次。
空间复杂度：O(1)，因为使用了常数个空间。
'''