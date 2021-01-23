'''
844. 比较含退格的字符串
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。
示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：
输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。

考查标签 双指针
'''


# 方法一：重构字符串
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res1 = []
        res2 = []
        for each in S:
            if each == '#':
                if res1:
                    res1.pop()
            else:
                res1.append(each)
        for each in T:
            if each == '#':
                if res2:
                    res2.pop()
            else:
                res2.append(each)
        if ''.join(res1) == ''.join(res2):
            return True
        else:
            return False
