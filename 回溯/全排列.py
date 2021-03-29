'''
全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
相关标签  回溯算法
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        backtrack(nums, [])
        return res
'''
代码讲解的网址：
https://leetcode-cn.com/problems/permutations/solution/46-quan-pai-lie-hui-su-fa-by-jue-qiang-z-jym3/
回溯法解决问题的过程，实际就是对一颗树的遍历过程
回溯法的三个基本要素：
1）路径：已经做出的选择；
2）选择列表：当前可以做出的选择；
3）结束条件：结束一次回溯算法的条件，即遍历到决策树的叶节点；
回溯法得解决问题得通用框架：
# 回溯算法，复杂度较高，因为回溯算法就是暴力穷举，遍历整颗决策树是不可避免的
结果 = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        结果.append(路径)
        return
    for 选择 in 选择列表:    # 核心代码段
        做出选择
        递归执行backtrack
        撤销选择
时间复杂度：O(N*N!)，N是序列nums的长度。

backtrack会被调用N!次，O(N!)：这部分的复杂度是回溯算法不可避免的，最开始for循环N次，随递归的进行，每次递归循环减1次，N*(N-1)(N-2)...*1 = N!）；
除了backtrack的调用，还包括列表的切片操作，O(N)；
'''