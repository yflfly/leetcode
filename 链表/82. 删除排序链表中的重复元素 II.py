'''
82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:
输入: 1->1->1->2->3
输出: 2->3
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newhead = ListNode(-1)
        p = newhead
        p.next = head
        cur = head
        while cur and cur.next:
            if cur.val != cur.next.val:
                p = p.next
                cur = cur.next
            else:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                p.next = cur
        return newhead.next
