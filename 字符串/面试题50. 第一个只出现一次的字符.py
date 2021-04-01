''''
面试题50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。
示例:
s = "abaccdeff"
返回 "b"
s = ""
返回 " "
'''


# 方法一：使用字典存储频数
class Solution:
    def firstUniqChar(self, s: str) -> str:
        d1 = {}
        for each in s:
            if each not in d1:
                d1[each] = 1
            else:
                d1[each] += 1
        for key in s:
            if d1[key] == 1:
                return key
        return ' '


'''
我们可以对字符串进行两次遍历。
在第一次遍历时，我们使用哈希映射统计出字符串中每个字符出现的次数。
在第二次遍历时，我们只要遍历到了一个只出现一次的字符，那么就返回该字符，否则在遍历结束后返回空格。
'''
