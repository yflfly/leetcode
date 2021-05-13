'''
961. 重复 N 次的元素
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
返回重复了 N 次的那个元素。
示例 1：
输入：[1,2,3,3]
输出：3
示例 2：
输入：[2,1,2,5,3,2]
输出：2
示例 3：
输入：[5,1,5,2,5,3,5,4]
输出：5
考查点：哈希表
'''


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums) // 2
        for each in nums:
            if each in dic:
                dic[each] += 1
                if dic[each] == n:
                    return each
            else:
                dic[each] = 1
