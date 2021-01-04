'''
合并K个排序链表
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
 
提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 方法一
'''
把链表都加入一个数组中，然后排序，再加到最后的链表中
此方法是常规思路，直接将所有的元素取出，然后排个序，再重组就达到了目的
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        for line in lists:
            while line:
                res.append(line.val)
                line = line.next
        if res == []:
            return None
        res.sort()
        l = ListNode(0)
        head = l
        for each in res:
            l.next = ListNode(each)
            l = l.next
        return head.next

# 方法二 优先队列(heap)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        import heapq
        heap = []
        # 首先 for 嵌套 while 就是将所有元素都取出放入堆中
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        # 依次将堆中的元素取出(因为是小顶堆，所以每次出来的都是目前堆中值最小的元素），然后重新构建一个列表返回
        while heap:
            temp_node = ListNode(heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next

# 方法三：分治法
'''
分治法可以通俗的解释为：把一片领土分解，分解为若干块小部分，然后一块块地占领征服，
被分解的可以是不同的政治派别或是其他什么，然后让他们彼此异化。
分治法的精髓：
分--将问题分解为规模更小的子问题；
治--将这些规模更小的子问题逐个击破；
合--将已解决的子问题合并，最终得出“母”问题的解；
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, node_a, node_b):
        dummy = ListNode(None)
        cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
        while cursor_a and cursor_b:  # 对两个节点的 val 进行判断，直到一方的 next 为空
            if cursor_a.val <= cursor_b.val:
                cursor_res.next = ListNode(cursor_a.val)
                cursor_a = cursor_a.next
            else:
                cursor_res.next = ListNode(cursor_b.val)
                cursor_b = cursor_b.next
            cursor_res = cursor_res.next
        # 有一方的next的为空，就没有比较的必要了，直接把不空的一边加入到结果的 next 上
        if cursor_a:
            cursor_res.next = cursor_a
        if cursor_b:
            cursor_res.next = cursor_b
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)

        # 边界情况
        if length == 0:
            return None
        if length == 1:
            return lists[0]

        # 分治
        mid = length // 2
        return self.merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length]))

