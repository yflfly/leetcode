# coding:utf-8
'''
93 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：
输入：s = "0000"
输出：["0.0.0.0"]
示例 3：
输入：s = "1111"
输出：["1.1.1.1"]
示例 4：
输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
'''

'''
全局变量：res = []
参数设计：（1）状态变量：当前组成的IP分割形式（2）条件变量：剩余字符 和 已组成的IP节个数。
完成条件：如果剩余的字符不能拼成一个IP，则返回；如果没有剩余字符，就加入到res。
递归过程：当前 字符 为一个合法IP节，则加入当前元素进入下一次递归。
'''


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []  # 定义全局变量保存最终结果
        state = []  # 定义状态变量保存当前状态
        deep = 0  # 定义条件变量（一般条件变量就是题目直接给的参数）

        def back(state, q, deep):
            if len(s) - q < 1 * (4 - deep) or len(s) - q > 3 * (4 - deep):  # 不满足合法条件（可以说是剪枝）
                return
            elif len(s) == q:  # 状态满足最终要求
                res.append(".".join([str(i) for i in state]))  # 加入结果
                return
            # 主要递归过程，一般是带有 循环体 或者 条件体
            for i in range(q, q + 3):  # 满足执行条件
                temp_num = int(s[q:i + 1])
                if len(str(temp_num)) != i - q + 1:
                    return
                if 0 <= int(s[q:i + 1]) <= 255:
                    back(state + [temp_num], i + 1, deep + 1)

        back(state, 0, deep)
        return res
