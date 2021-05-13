'''
884. 两句话中的不常见单词
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
返回所有不常用单词的列表。
您可以按任何顺序返回列表。
示例 1：
输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
示例 2：
输入：A = "apple apple", B = "banana"
输出：["banana"]
考查点：哈希表
'''


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic = {}
        for word in s1.split():
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        for word in s2.split():
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        res = []
        for key in dic:
            if dic[key] == 1:
                res.append(key)
        return res
