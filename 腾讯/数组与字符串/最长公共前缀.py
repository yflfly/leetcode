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


# 方法二：纵向扫描
'''
方法一是横向扫描，依次遍历每个字符串，更新最长公共前缀。
另一种方法是纵向扫描。纵向扫描时，从前往后遍历所有字符串的每一列，比较相同列上的字符是否相同，
如果相同则继续对下一列进行比较，如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀。

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # 若列表为空 则返回空，即输入不存在公共前缀
            return ""
        len_1 = len(strs[0])
        len_all = len(strs)
        for i in range(len_1):
            str1 = strs[0][i]
            for j in range(1, len_all):
                if i == len(strs[j]) or strs[j][i] != str1:
                    return strs[0][:i]
        return strs[0]

