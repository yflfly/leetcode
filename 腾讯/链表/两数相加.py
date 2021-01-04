'''
 两数相加
 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方法一：将链表的值转换成整数，整数相加，然后再进行逆序创建一个新的链表
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_1 = ''
        while l1:
            sum_1 += str(l1.val)
            l1 = l1.next
        sum_2 = ''
        while l2:
            sum_2 += str(l2.val)
            l2 = l2.next
        int_1 = int(sum_1[::-1])
        int_2 = int(sum_2[::-1])
        int_3 = int_1 + int_2
        sum_3 = str(int_3)[::-1]
        l3 = ListNode(sum_3[0])
        cur = l3
        for i in range(1, len(sum_3)):
            linshi = ListNode(sum_3[i])
            cur.next = linshi
            cur = cur.next
        return l3


# 方法二：进位进行相加
'''
同时遍历两个链表
同步创建结果链表
'''


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)  # 结果链表的dummy节点
        cur = dummyHead
        carry = 0
        while l1 or l2:  # 只要有一个链表未结束，继续遍历
            valL1 = l1.val if l1 else 0  # 结束的链表赋值0
            valL2 = l2.val if l2 else 0
            total = valL1 + valL2 + carry
            carry = total // 10  # 进位处理
            cur.next = ListNode(total % 10)
            cur = cur.next  # 结果链表创建
            if l1:  # 只遍历未结束的链表，结束的上面直接赋值0
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:  # 不要忘记最后退出循环后，进位的处理
            cur.next = ListNode(carry)
        return dummyHead.next
