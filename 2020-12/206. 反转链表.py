# coding:utf-8
'''
206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        list1 = []
        while head:
            list1.insert(0, head.val)
            head = head.next
        pre = ListNode(0)
        node_start = pre
        for i in range(len(list1)):
            node_start.val = list1[i]
            if i != len(list1) - 1:
                node_start.next = ListNode(0)
            else:
                node_start.next = None
        return node_start


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
