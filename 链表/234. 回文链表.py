'''
234. 回文链表
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        str1 = ''.join(list1)
        str2 = ''.join(list1.reverse())
        if str1 == str2:
            return True
        else:
            return False


# 快慢指针的方法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if (head is None) or (head.next is None):
            return True
        slow = head
        fast = head
        pre = head
        prepre = ListNode(None)

        while (fast and fast.next):
            pre = slow  # pre 紧跟在slow 后面一步

            slow = slow.next  # 快慢指针用于找到中间节点
            fast = fast.next.next

            pre.next = prepre  # 用于反转前半部分链表
            prepre = pre

        if (fast):  # 如果跳出上一个while循环是 fast.next is None,那么就是奇数个节点，slow需要再走一步
            slow = slow.next

        while (pre and slow):  # 从中间对称的位置往两边扩展，比对两边的数是否相等
            if (pre.val != slow.val):
                return False
            pre = pre.next
            slow = slow.next
        return True


# 方法一：双指针
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if (head is None) or (head.next is None):
            return True
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        i, j = 0, len(tmp) - 1
        while i != j and i < len(tmp):
            if tmp[i] != tmp[j]:
                return False
            i += 1
            j -= 1
        return True


'''
将链表的数存储到列表中，在列表中利用双指针的方法
'''
