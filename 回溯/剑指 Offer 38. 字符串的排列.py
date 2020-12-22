# coding:utf-8
'''
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
'''


class Solution:
    def permutation(self, s: str) -> List[str]:
        length = len(s)
        if length == 1:
            return [s]  # 边界
        else:
            res = []
            for i in range(length):
                ch = s[i]  # 取出s中每一个字符
                rest = s[:i] + s[i + 1:]
                for x in self.permutation(rest):  # 递归
                    res.append(ch + x)  # 将ch 和子问题的解依次组合
        return list(set(res))


class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue  # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res
'''
out = set()


def Permutation(ss):
    if len(ss) == 0:
        return out
    charlist = list(ss)
    permutation(charlist, 0, out)
    return sorted(list(out))


def permutation(ss, begin, out):
    if begin == len(ss) - 1:
        out.add(''.join(ss[:]))
    else:
        for i in range(begin, len(ss)):
            # 如果是重复字符，跳过
            if ss[begin] == ss[i] and begin != i:
                continue
            else:
                # 依次与后面每个字符交换
                ss[begin], ss[i] = ss[i], ss[begin]
                print(ss)
                permutation(ss, begin + 1, out)
                # 回到上一个状态
                ss[begin], ss[i] = ss[i], ss[begin]
s = "abc"
print(Permutation(s))
'''