'''
127. 单词接龙
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：
序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。
示例 1：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
示例 2：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。

考查点：广度优先搜索 BFS
'''


# 方法 BFS 广度优先搜索

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        if beginWord == endWord:
            return 0
        q, visited = [(beginWord, 1)], set()
        while q:
            word, step = q.pop(0)
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return step
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = word[:i] + j + word[i + 1:]
                        if tmp in wordDict and tmp not in visited:  # difference
                            q.append((tmp, step + 1))
        return 0


'''
由于是求最短路径，很容易想到通过广度优先遍历来解决这个问题。
现在要解决的问题就变成了如何判断两个单词只有一个字母不同，最简单的办法就是通过26个字母替换。
'''

'''
讲解参考网址：
https://blog.csdn.net/qq_17550379/article/details/83652490
'''