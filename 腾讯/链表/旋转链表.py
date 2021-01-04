'''
旋转链表
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一：先组成环，然后再拆环
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:  # 链表为空，返回为空
            return None
        if not head.next:  # 链表只有一个节点，则返回该节点
            return head
        # 将链表形成一个环形
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 将环拆开
        new_tail.next = None

        return new_head


# 方法二：快慢指针
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k:
            return head
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        k = k % count
        if k == 0:
            return head
        fast = head
        slow = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead
