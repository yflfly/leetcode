# coding:utf-8
'''
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        result = ListNode(0)
        result.next = head
        res = result
        for _ in range(m):
            pre = res
            res = res.next

        back = res
        temp1 = None
        temp2 = None
        for _ in range(n - m + 1):
            temp1 = res.next
            res.next = temp2
            temp2 = res
            res = temp1

        pre.next = temp2
        back.next = temp1
        return result.next

