# coding:utf-8
'''
剑指 Offer 22. 链表中倒数第k个节点
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，
本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 将链表中的每一个节点都放到一个列表中。-k即为要查找的节点

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        result = []
        while head:
            result.append(head)
            head = head.next
        return result[-k]


'''

算法流程：
初始化： 前指针 former 、后指针 latter ，双指针都指向头节点 head​ 。
构建双指针距离： 前指针 former 先向前走 kk 步（结束后，双指针 former 和 latter 间相距 kk 步）。
双指针共同移动： 循环中，双指针 former 和 latter 每轮都向前走一步，直至 former 走过链表 尾节点 时跳出（跳出后， latter 与尾节点距离为 k-1k−1，即 latter 指向倒数第 kk 个节点）。
返回值： 返回 latter 即可。
讲解网址：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solution/mian-shi-ti-22-lian-biao-zhong-dao-shu-di-kge-j-11/
'''


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head  or k == 0:
            return
        pre = head
        later = head
        for i in range(k):
            if not pre:  # 当k大于链表的长度
                return
            pre = pre.next
        while pre:
            pre = pre.next
            later = later.next
        return later


'''
时间复杂度：O(N)，其中N为链表长度。
空间复杂度：O(1)
'''
