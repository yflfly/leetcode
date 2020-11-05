# coding:utf-8

'''
1209. 删除字符串中的所有相邻重复项 II

给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
在执行完所有删除操作后，返回最终得到的字符串。
本题答案保证唯一。

示例 1：

输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。
示例 2：

输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"
示例 3：

输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"
 

提示：

1 <= s.length <= 10^5
2 <= k <= 10^4
s 中只含有小写英文字母。

'''

# 本人的方法(运行超时)：
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        for i in range(len(s)):
            if len(res) < k - 1:
                res.append(s[i])
            else:
                tag = 0
                for j in range(1, k):
                    if s[i] != res[-j]:
                        tag += 1
                if tag == 0:
                    res = res[:-k+1]
                else:
                    res.append(s[i])
        return ''.join(res)

'''
# 别人的方法 运行通过
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        pre = ''
        for ch in s:
            if pre == '' or ch != pre:
                res.append((ch, 1))
                pre = ch
            else:
                times = res[-1][1] + 1
                if times == k:
                    tp_k = k - 1
                    while tp_k > 0:
                        res.pop()
                        tp_k -= 1
                    if res == []:
                        pre = ''
                    else:
                        pre = res[-1][0]
                else:
                    res.append((ch, times))
        out = ""
        for rs in res:
            out += rs[0]
        return out

'''

