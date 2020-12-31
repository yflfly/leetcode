'''
面试题 02.04. 分割链表
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。
示例:
输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        while head:
            if head.val < x:
                before.next = head  # before_head的下一个指向head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None  # 将after尾部指向空
        before.next = after_head.next  # 将before的下一个指向after_head的下一个
        return before_head.next


'''
首先用before和after两个指针分别存储小于、大于x的节点，两节点不断更新(与head同时更新)直至到达尾部，而再用两个哨兵节点before_head和after_head存储最开始的头节点，通过这二者进行连接。
'''
