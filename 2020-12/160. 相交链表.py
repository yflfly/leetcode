# coding:utf-8
'''
160. 相交链表
编写一个程序，找到两个单链表相交的起始节点。


网址：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        nodeA = headA
        nodeB = headB
        while (nodeA != nodeB):
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA
