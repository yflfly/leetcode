'''
28. 实现 strStr()
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''


# 方法一：子串逐一比较-线性时间复杂度
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for start in range(n - m + 1):
            if haystack[start:start + m] == needle:
                return start
        return -1


'''
复杂度分析
时间复杂度：O((N−L)L)，其中N为haystack字符串的长度，L为needle字符串的长度。内循环中比较字符串的复杂度为 L，总共需要比较(N - L)次。
空间复杂度：O(1)

'''

# 方法二：KMP算法
''' 
步骤如下所示：
1）初始化next数组
2）处理前后缀不相同的情况
3）处理前后缀相同的情况
4）更新next数组
例子
aabaabaaf    aabaaf
next 0 1 0 1 2 0
'''
'''
KMP的经典思想就是：当出现字符串不匹配时，可以记录一部分之前已经匹配的文本内容，利用这些信息避免从头再去做匹配

KMP解决字符串匹配的问题
文本串  aabaabaaf
模式串  aabaaf

前缀表
求一个字符串 最长相等前后缀

前缀？后缀？
例子：aabaaf
前缀：包含首字母 不包含尾字母的所有子串 a aa aab aaba aabaa
后缀：包含尾字母 不包含首字母的所有子串 f af aaf baaf abaaf

求最长相等前后缀
a       0
aa      1  前缀 a  后缀 a
aab     0  前缀 a aa  后缀 b ab
aaba    1  前缀 a aa aab 后缀 a  ba aba
aabaa   2  前缀 a aa aab aaba  后缀 a aa baa abaa 
aabaaf  0  前缀 a aa aab aaba  aabaa 后缀 f af aaf baaf abaaf
得到一个序列 0 1 0 1 2 0

即得到字符串的前缀表：
a a b a a f
0 1 0 1 2 0
实现KMP算法 会将前缀表统一后移或者减1操作  原理是一样的
'''


#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        if not haystack and needle:
            return -1
        if haystack and not needle:
            return 0
        def buildnext(p):
            next = []
            next.append(0)  # next[0]必然是0
            x = 1  # 从next[1]开始求
            now = 0
            while x < len(p):
                if p[now] == p[x]:
                    now += 1
                    x += 1
                    next.append(now)
                elif now:
                    now = next[now - 1]  # 缩小 now,改成next[now-1]
                else:
                    next.append(0)  # now已经为0，无法再缩，故next[x]= 0
                    x += 1
            return next

        tar = 0  # 主串中将要匹配得位置
        pos = 0  # 模式串中将要匹配得位置
        next = buildnext(needle)
        while tar < len(haystack):
            if haystack[tar] == needle[pos]:
                tar += 1
                pos += 1
            elif pos:
                pos = next[pos - 1]
            else:
                tar += 1
            if pos == len(needle):
                return tar - pos
        return -1

# 获取next数组
def buildnext(p):
    next = []
    next.append(0)  # next[0]必然是0
    x = 1  # 从next[1]开始求
    now = 0

    while x < len(p):
        if p[now] == p[x]:
            now += 1
            x += 1
            next.append(now)
        elif now:
            now = next[now - 1]  # 缩小 now,改成next[now-1]
        else:
            next.append(0)  # now已经为0，无法再缩，故next[x]= 0
            x += 1
    return next


# 匹配
def search(s, p):
    tar = 0  # 主串中将要匹配得位置
    pos = 0  # 模式串中将要匹配得位置
    next = buildnext(p)
    while tar < len(s):
        if s[tar] == p[pos]:  # 若两个字符相等，则tar、pos各进一步
            tar += 1
            pos += 1
        elif pos:  # 失配了，若pos!=0，则依据next数组移动标尺
            pos = next[pos - 1]
        else:  # pos[0]失配了，直接把标尺右移一位
            tar += 1
        if pos == len(p):  # pos走到了len(p)，匹配成功
            return tar - pos
            # pos = next[pos - 1]

    return -1


# p = 'aabaaf'
# print(buildnext(p))  # [0, 1, 0, 1, 2, 0]
haystack = "hello"
needle = "ll"

print(search(haystack, needle))
