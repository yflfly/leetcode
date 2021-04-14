# coding:utf-8
'''
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(list(set(list(s)))) == 1:
            return 1
        dict1 = {}
        for i in range(len(s)):
            str1 = s[i]
            tag = 0
            for j in range(i + 1, len(s)):
                if s[j] not in str1:
                    str1 = str1 + s[j]
                else:
                    if str1 not in dict1:
                        dict1[str1] = len(str1)
                    tag = 1
                    break
            if tag == 0:
                dict1[str1] = len(str1)
        list1 = dict1.values()
        max1 = 0
        for each in list1:
            if each > max1:
                max1 = each
        return max1


def get_substring(s):
    if len(s) == 0:
        return 0
    if len(list(set(list(s)))) == 1:
        return 1
    dict1 = {}
    for i in range(len(s)):
        str1 = s[i]
        tag = 0
        for j in range(i + 1, len(s)):
            if s[j] not in str1:
                str1 = str1 + s[j]
            else:
                if str1 not in dict1:
                    dict1[str1] = len(str1)
                tag = 1
                break
        if tag == 0:
            dict1[str1] = len(str1)
    list1 = dict1.values()
    max1 = 0
    for each in list1:
        if each > max1:
            max1 = each
    return max1


# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = -1
        res = 0
        dict = {}
        for right, item in enumerate(s):
            if item in dict and dict[item] > left:  # 字符 item 在字典中, 且上次出现的下标 > 当前长度的左下标
                left = dict[item]  # 左下标移动到上次出现的位置，已经出现重复，肯定长度不会更大了，所以移动左下标
                dict[item] = right  # 更新那个再次出现的元素的新下标
            else:  # 不在字典中
                dict[item] = right  # 添加元素
                res = max(res, right - left)
        return res


# 暴力求解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        res = 0
        for i in range(len(s)):
            str_tmp = s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in str_tmp:
                    str_tmp = str_tmp + s[j]
                else:
                    break
            res = max(res, len(str_tmp))
        return res
