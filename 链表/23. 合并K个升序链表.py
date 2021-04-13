'''
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：
输入：lists = []
输出：[]
示例 3：
输入：lists = [[]]
输出：[]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]

        mid = n // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))

    # 迭代写法
    def mergeTwoLists(self, node1, node2):
        dummy = cur = ListNode()
        while node1 and node2:
            if node1.val <= node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next

        cur.next = node1 if node1 else node2
        return dummy.next
'''
归并排序：先两两合并mergeTwoLists，然后对已经经过一次两两合并的链表们再进行一次两两合并，一直合并到生成最终的升序链表为止
mergeKLists步骤如下：
特判（即递归终止条件）：如果待合并的链表个数为0返回空，个数为1返回lists[0]无需合并
当待合并的链表个数大于等于2时，调用mergeTwoLists进行两两合并
这里mergeTwoLists的两个参数采用递归mergeKLists的方式，也就是对已经合并好的lists前一半的链表和后一半的链表进行合并，如果没合并好，先分别合并了再最终合并
'''