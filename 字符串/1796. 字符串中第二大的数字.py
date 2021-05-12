'''
1796. 字符串中第二大的数字
给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
混合字符串 由小写英文字母和数字组成。
示例 1：
输入：s = "dfa12321afd"
输出：2
解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
示例 2：
输入：s = "abc1111"
输出：-1
解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
'''


class Solution:
    def secondHighest(self, s: str) -> int:
        res = []
        for each in s:
            if each.isdigit():
                res.append(int(each))
        res = sorted(list(set(res)))
        if len(res) < 2:
            return -1
        else:
            return int(res[-2])
