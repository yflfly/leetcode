'''
8.字符串转换整数 (atoi)
请你来实现一个 atoi 函数，使其能将字符串转换成整数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0 。

注意：
本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  231 − 1 或 −231 。
示例 1:
输入: "42"
输出: 42
示例 2:
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。

考查标签：数学、字符串
'''


class Solution:
    def myAtoi(self, str: str) -> int:
        nums = ['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = []
        str_list = list(str)
        for i in range(len(str_list)):
            if str_list[i] == ' ':
                continue
            elif str_list[i] in nums:
                res.append(str_list[i])
            else:
                break
        if not res:
            return 0
        res_1 = []
        flag = 1
        for each in res:
            if each == '-':
                flag = -1
            if each == '-' or each == '+':
                continue
            res_1.append(each)
        res_int = int(''.join(res_1))
        if res_int * flag > (2 ** 31) - 1:
            return (2 ** 31) - 1
        if res_int * flag < -2 ** 31:
            return -2 ** 31
        return res_int * flag


class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        n = len(str)
        while i < n and str[i] == ' ':
            i = i + 1
        if n == 0 or i == n:
            return 0
        flag = 1
        if str[i] == '-':
            flag = -1
        if str[i] == '+' or str[i] == '-':
            i = i + 1
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        ans = 0
        while i < n and '0' <= str[i] <= '9':
            ans = ans * 10 + int(str[i]) - int('0')
            i += 1
            if (ans - 1 > INT_MAX):
                break

        ans = ans * flag
        if ans > INT_MAX:
            return INT_MAX
        return INT_MIN if ans < INT_MIN else ans


# ------------------下面的方法是别人的方法------------------------
# 方案一，传统思维方式，思考过程见注释
# 该方案战胜 72.56 % 的 python3 提交记录
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()  # 去掉左边多余空格
        if str == "":  # 如果字符串为空，返回0
            return 0
        res, sign = 0, 1  # 结果初值为0，符号位初值为1
        if str[0] == "+" or str[0] == "-":  # 字符串如果以正负号开始，记下符号位
            sign = -1 if str[0] == "-" else 1
            start = 1  # 如果有正负号，从下标1开始转换
        else:
            start = 0  # 如果没有正负号，从下标0开始转换
        for i in range(start, len(str)):
            if str[i].isdigit():
                res = res * 10 + int(str[i])  # 将数字字符的值累加进结果
            else:
                break
        res = res * sign  # 根据符号位，还原结果的正负
        if res > 2 ** 31 - 1:  # 这个if是用来返回大小超限的结果
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31
        else:
            return res


# 方案二，使用正则表达式，这玩意儿厉害了！同时，还需要星号表达式来帮忙处理找不到匹配项返回0的问题。
# 该方案战胜 94.46 % 的 python3 提交记录
class Solution:
    def myAtoi(self, str: str) -> int:
        """
        对下面语句中的正则表达式做个解释：
        ^：上尖号放在最前面表示所查找的内容必须在字符串的开头，效果是忽略字符串中其他位置的匹配项
        [\+\-]：方括号表示匹配其中的任一字符，效果就是匹配加号或者减号
        ?：问号表示前面匹配的那个字符可有可无，效果就是可能没有符号
        \d：这个是固定用法，表示一个数字
        +：加号表示前面字符的出现次数可以是一个或多个，效果是匹配任意长度的数字
        """
        import re
        # 因为findall函数返回的是一个列表，要将其中的内容取出来必须使用星号表达式(*)
        # 使用星号表达式的好处是：如果没有匹配项，即对于空列表[]使用星号表达式取整，结果为0
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2 ** 31 - 1), -2 ** 31)


# 以下是本地测试代码，提交时只需复制上面的代码块即可
# solution = Solution()
# print(solution.myAtoi("42"))
# print(solution.myAtoi("   -42"))
# print(solution.myAtoi("4193 with words"))
# print(solution.myAtoi("words and 987"))
# print(solution.myAtoi("-91283472332"))
# print(solution.myAtoi("  0000000000012345678"))
