'''
409. 最长回文串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。
示例 1:
输入:
"abccccdd"
输出:
7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        l_s = list(s)
        # 字典来存储每个字母出现的个数
        m = {}
        for word in l_s:
            if word not in m:
                m[word] = 1
            else:
                m[word] += 1
        result = 0
        for key, value in m.items():
            # 如果出现个数为偶数，直接加入
            if value % 2 == 0:
                result += value
            else:
                # 如果为奇数，则加value - 1，并且，该字母的次数变为1
                result += value - 1
                m[key] = 1  # 关键行，处理例如："aaabb"-转化为->"ababa"
        # 如果遍历完成的字符串中还有，出现值为1的字母，那么结果长度还要加1才行，因为可以把这个单个字母放在中间，使长度再增加1
        return result + 1 if 1 in m.values() else result
