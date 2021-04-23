'''
567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
示例 1：
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：
输入: s1= "ab" s2 = "eidboaoo"
输出: False
提示：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
'''
import collections


class Solution(object):
    def checkInclusion(self, s1, s2):
        counter_1 = collections.Counter(s1)
        n = len(s2)
        left = 0
        right = len(s1) - 1
        counter_2 = collections.Counter(s2[0:right])

        while right < n:
            counter_2[s2[right]] += 1
            if counter_1 == counter_2:
                return True
            counter_2[s2[left]] -= 1

            if counter_2[s2[left]] == 0:
                del counter_2[s2[left]]

            left += 1
            right += 1
        return False


s1 = "ab"
s2 = "ba"
counter_1 = collections.Counter(s1)
counter_2 = collections.Counter(s2)
counter_2['e'] += 1
print(counter_1)
print(counter_2)
print(type(counter_2))
if counter_1 == counter_2:
    print(11111111)