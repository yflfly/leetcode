'''
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true

考查标签  栈、字符串
'''


class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')': '(', '}': '{', ']': '['}
        res = []
        for i in range(len(s)):
            if not res:
                res.append(s[i])
            elif s[i] in dict1:
                if dict1[s[i]] == res[-1]:
                    res.pop()
                else:
                    res.append(s[i])
            else:
                res.append(s[i])
        if not res:
            return True
        else:
            return False


a = Solution()
s = "{[]}"
print(a.isValid(s))
