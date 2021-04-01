'''
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false
'''


# str.isalpha() 所有字符都是字母
# str.isdigit() 所有字符都是数字，如果带小数点，则会返回False

def isPalindrome(s):
    str1 = ''
    for each in s:
        if each.isalpha() or each.isdigit():
            str1 = str1 + str(each.lower())
    list1 = list(str1)
    list1.reverse()
    str2 = ''.join(list1)
    if str1 == str2:
        return True
    else:
        return False


s = "A man, a plan, a canal: Panama"
s = "race a car"
print(isPalindrome(s))

# 双指针
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = ''.join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left = 0
        right = n-1
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left += 1
            right -= 1
        return True
'''
复杂度分析
时间复杂度：O(∣s∣)，其中∣s∣ 是字符串s的长度。
空间复杂度：O(∣s∣)。由于我们需要将所有的字母和数字字符存放在另一个字符串中，在最坏情况下，新的字符串sgood 与原字符串s 完全相同，因此需要使用O(∣s∣) 的空间。
'''