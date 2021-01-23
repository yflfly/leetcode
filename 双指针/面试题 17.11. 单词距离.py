'''
面试题 17.11. 单词距离
有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。
如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：
输入：words = ["I","am","a","student","from","a","university","in","a","city"],
 word1 = "a", word2 = "student"
输出：1

考查标签：双指针
'''


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        index1 = float('-inf')
        index2 = float('-inf')
        res = len(words)
        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            res = min(res, abs(index2 - index1))
        return res
