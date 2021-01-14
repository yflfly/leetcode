'''
最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

考查标签  字符串
'''


# 方法一：横向扫描

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # 若列表为空 则返回空，即输入不存在公共前缀
            return ""

        def lcp(str1, str2):
            length = min(len(str1), len(str2))
            index = 0
            while index < length and str1[index] == str2[index]:
                index += 1
            return str1[:index]

        pre = strs[0]
        len_str1 = len(strs)
        for i in range(1, len_str1):
            pre = lcp(pre, strs[i])
            if not pre:  # 当不存在公共前缀时，则剪枝，不进行后续的循环判断
                break
        return pre


'''
代码讲解网址：
https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
'''
