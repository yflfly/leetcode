# coding:utf-8
'''
1669. 合并两个链表
给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。

请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。

题目网址：
https://leetcode-cn.com/problems/merge-in-between-linked-lists/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        flag = 0
        ind = list1
        while flag < a - 1:
            ind = ind.next
            flag += 1
        flag += 1
        ind1 = ind
        for i in range(int(b - a + 1)):
            ind1 = ind1.next
            ind.next = ind.next.next
        ind1 = ind1.next
        ind.next = list2
        ind2 = ind
        while ind2.next != None:
            ind2 = ind2.next
        ind2.next = ind1
        return list1
