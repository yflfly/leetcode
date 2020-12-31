'''
面试题 02.02. 返回倒数第 k 个节点
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
注意：本题相对原题稍作改动
示例：
输入： 1->2->3->4->5 和 k = 2
输出： 4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 方法一
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        pre = head
        later = head
        for i in range(k):
            pre = pre.next
        while pre:
            pre = pre.next
            later = later.next
        return later.val

# 方法二
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        return list1[-k]