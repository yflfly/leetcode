'''
面试题 02.03. 删除中间节点
实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。
示例：
输入：单向链表a->b->c->d->e->f中的节点c
结果：不返回任何数据，但该链表变为a->b->d->e->f
'''
'''
解题思路：
如果只能访问当前节点，那么该题的解题思路就是，将自己变成其他节点。
举个例子：A->B->C->D
如果要删掉 B 节点，那么只需要将 B 变为 C，再把 B 的指针指向 D，即可完成。

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            if node.next.next:
                node.next = node.next.next
            else:
                node.next = None