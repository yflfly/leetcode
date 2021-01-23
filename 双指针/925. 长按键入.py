'''
925. 长按键入
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：
输入：name = "leelee", typed = "lleeelee"
输出：true
示例 4：
输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。

考查标签：双指针
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name)


'''
字符串typed的每个字符，有且只有两种用途：
1）作为name的一部分，此时会匹配name中的一个字符
2）作为长按键入的一部分，此时它应当与前一个字符相同

如果typed 中存在一个字符，它两个条件均不满足，则应当直接返回 false；否则，当typed 扫描完毕后，我们再检查name 的每个字符是否都被「匹配」了。
实现上，我们使用两个下标i,j追踪name和typed 的位置。
当name[i]=typed[j] 时，说明两个字符串存在一对匹配的字符，此时将 i,j 都加1。
否则，如果typed[j]=typed[j−1]，说明存在一次长按键入，此时只将j加1。
最后，如果i=name.length，说明name 的每个字符都被「匹配」了。

代码讲解的网址：
https://leetcode-cn.com/problems/long-pressed-name/solution/chang-an-jian-ru-by-leetcode-solution/
'''
