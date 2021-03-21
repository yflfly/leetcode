'''
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一：从头到尾将链表打印到数组中，返回反转后的结果即可
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res_lst = []
        if not head:
            return []
        while head:
            res_lst.append(head.val)
            head = head.next
        return res_lst[::-1]


'''
复杂度分析
时间复杂度：O(n)，reverse() 的时间复杂度为O(n)，遍历了一遍数组，复杂度也为O(n)
空间复杂度：O(n)，使用了额外的res。
'''


# 方法二：递归
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        return self.reversePrint(head.next) + [head.val]


'''
复杂度分析
时间复杂度：O(n)，递归n次，时间间复杂度为O(n)，递归函数中的操作时间复杂度为O(1)，总时间复杂度为O(n)O(n)×O(1)=O(n)。
空间复杂度：O(n)，递归将占用链表长度的栈空间。
递归存在一个问题：当链表非常长的时候，就会导致函数调用的层级很深，从而有可能导致函数调用栈溢出
'''


# 方法三：借助栈
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:  # push
            stack.append(head.val)
            head = head.next
        res = []
        while stack:  # pop
            res.append(stack.pop())
        return res


'''
利用堆栈先进后出的特点，先依次将元素压入堆栈中，然后将所有元素从堆栈中弹出，即可实现反转
复杂度分析
时间复杂度：O(n)，pushpush 的间复杂度为O(n)，pop的间复杂度为O(n)。
空间复杂度：O(n)，使用了额外的res和堆栈。

'''
