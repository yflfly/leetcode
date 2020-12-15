# coding:utf-8
'''
345. 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
示例 1：
输入："hello"
输出："holle"
示例 2：
输入："leetcode"
输出："leotcede"
提示：
元音字母不包含字母 "y" 。
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        yuanyin = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        left = 0
        right = len(s_list) - 1
        while left < right:
            if s_list[left] in yuanyin and s_list[right] in yuanyin:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            if s_list[right] not in yuanyin:
                right -= 1
            if s_list[left] not in yuanyin:
                left += 1
        return ''.join(s_list)