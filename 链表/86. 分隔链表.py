'''
86. 分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置。
示例 1：
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：
输入：head = [2,1], x = 2
输出：[1,2]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_list = ListNode(0)
        smll_head = small_list
        large_list = ListNode(0)
        large_head = large_list
        cur = head
        while cur:
            if cur.val < x:
                tmp = ListNode(cur.val)
                small_list.next = tmp
                small_list = small_list.next
            else:
                tmp = ListNode(cur.val)
                large_list.next = tmp
                large_list = large_list.next
            cur = cur.next
        small_list.next = large_head.next

        return smll_head.next
