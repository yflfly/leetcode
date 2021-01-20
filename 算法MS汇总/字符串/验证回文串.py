'''
验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false

考查标签：双指针 字符串
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isdigit() or s[left].isalpha():
                if s[right].isdigit() or s[right].isalpha():
                    if s[left].lower() == s[right].lower():
                        left += 1
                        right -= 1
                    else:
                        return False
                else:
                    right -= 1
            else:
                left += 1
        return True