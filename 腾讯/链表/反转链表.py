# coding:utf-8
'''
题目：反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一：双指针
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


# 方法二：递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur:
                return pre  # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回


'''
两种方法的讲解地址：
https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/jian-zhi-offer-24-fan-zhuan-lian-biao-die-dai-di-2/
'''
