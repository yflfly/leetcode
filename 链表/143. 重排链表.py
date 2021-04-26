'''
143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        tmp_list = []
        if not head:
            return
        cur = head
        while cur:
            tmp_list.append(cur)
            cur = cur.next
        i, j = 0, len(tmp_list) - 1
        while i < j:
            tmp_list[i].next = tmp_list[j]
            i += 1
            if i == j:
                break
            tmp_list[j].next = tmp_list[i]
            j -= 1
        tmp_list[i].next = None


'''
线性表
因为链表不支持下标访问，所以我们无法随机访问链表中任意位置的元素。
因此比较容易想到的一个方法是，我们利用线性表存储该链表，然后利用线性表可以下标访问的特点，直接按顺序访问指定元素，
重建该链表即可。
复杂度分析
时间复杂度：O(N)，其中N是链表中的节点数。
空间复杂度：O(N)，其中N是链表中的节点数。主要为线性表的开销。
'''
