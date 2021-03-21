'''
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."
'''


# 方法一：调用已有的函数 面试等着挂吧
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


# 方法二：双指针法
class Solution:
    def replaceSpace(self, s: str) -> str:
        count = 0  # 对字符串中的空格进行统计
        for each in s:
            if each == ' ':
                count += 1
        if count == 0:
            return s
        s_lst = list(s)
        for i in range(count * 2):
            s_lst.append('')
        p1 = len(s) - 1
        p2 = len(s_lst) - 1
        while p1 != p2:
            if s_lst[p1] != ' ':
                s_lst[p2] = s_lst[p1]
                p1 -= 1
                p2 -= 1
            else:
                s_lst[p2] = '0'
                s_lst[p2 - 1] = '2'
                s_lst[p2 - 2] = '%'
                p2 -= 3
                p1 -= 1
        return ''.join(s_lst)
