# coding:utf-8
'''
1669. 合并两个链表
给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。
请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。
示例 1：
输入：list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
输出：[0,1,2,1000000,1000001,1000002,5]
解释：我们删除 list1 中第三和第四个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。
示例 2：
输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
输出：[0,1,1000000,1000001,1000002,1000003,1000004,6]
解释：上图中蓝色的边和节点为答案链表。

题目网址：
https://leetcode-cn.com/problems/merge-in-between-linked-lists/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        flag = 0
        begin_1 = list1
        while flag < a - 1:
            begin_1 = begin_1.next
            flag += 1

        end_1 = begin_1
        for i in range(int(b - a + 1)):
            end_1 = end_1.next

        end_1 = end_1.next
        begin_1.next = list2
        begin_2 = begin_1
        while begin_2.next != None:
            begin_2 = begin_2.next
        begin_2.next = end_1
        return list1
'''
复杂度分析：
时间复杂度：O(m + n)，m 为 list1 中节点的个数，n 为 list2 中节点的个数。
空间复杂度：O(1)
'''