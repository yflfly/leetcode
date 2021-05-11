'''
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
示例：
s = "leetcode"
返回 0
s = "loveleetcode"
返回 2
考查点：哈希表、字符串
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for each in s:
            if each in dic:
                dic[each] += 1
            else:
                dic[each] = 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
