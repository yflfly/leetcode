'''
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：
输入：head = [1], n = 1
输出：[]
示例 3：
输入：head = [1,2], n = 1
输出：[1]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一 暴力求解法
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lengths = 0
        node = head
        while node:
            lengths += 1
            node = node.next
        dummy = ListNode(0, head)
        cur = dummy
        for i in range(1, lengths - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


# 方法二：快慢指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

