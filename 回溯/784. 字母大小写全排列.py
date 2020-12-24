# coding:utf-8
'''
784. 字母大小写全排列
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]
输入：S = "3z4"
输出：["3z4", "3Z4"]
输入：S = "12345"
输出：["12345"]
'''


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        S = list(S)
        self.helper(S, 0, res)
        return res

    def helper(self, S, i, res):
        if i >= len(S):
            res.append("".join(S))
            return
        c = ord(S[i])
        if c >= 65 and c <= 90:
            self.helper(S, i + 1, res)
            S[i] = S[i].lower()
            self.helper(S, i + 1, res)
        elif c >= 97 and c <= 122:
            self.helper(S, i + 1, res)
            S[i] = S[i].upper()
            self.helper(S, i + 1, res)
        else:
            self.helper(S, i + 1, res)

'''
代码讲解网址：
https://www.cnblogs.com/xiximayou/p/12458703.html
核心：还是递归加回溯。注意字符的ASCII码值：A:65,Z:90,a:97,z:122。以及python中字符串是不可变数据类型，要转换成列表进行操作。

如果是数字，继续遍历下一位
如果是小写字母：1）继续遍历下一位；2）转换成大写，再继续遍历下一位
如果是大写字母：1）继续遍历下一位；2）转换成小写，再继续遍历下一位

将每一个结果都添加到结果中

'''
