'''
面试题 17.22. 单词转换
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。
编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。
示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出:
["hit","hot","dot","lot","log","cog"]
示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: []
解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
'''

# 广度优先搜索
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # 单向BFS
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        L = len(beginWord)

        d = defaultdict(set)
        for word in wordSet:
            for i in range(L):
                d[word[:i] + '*' + word[i + 1:]].add(word)

        visited = {beginWord: beginWord}  # 记录已访问过的字符串及其父项
        stack = {beginWord}
        while stack:
            next_level_stack = set()
            for word in stack:
                for i in range(L):
                    connected_words = d[word[:i] + '*' + word[i + 1:]]
                    if endWord in connected_words:  # stop criterion
                        path = [word]
                        while word != beginWord:
                            word = visited[word]
                            path.append(word)
                        return path[::-1] + [endWord]
                    for cword in connected_words:
                        if cword not in visited:
                            visited[cword] = word
                            next_level_stack.add(cword)
            stack = next_level_stack
        return []
