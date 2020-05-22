#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (41.21%)
# Likes:    450
# Dislikes: 0
# Total Accepted:    75.9K
# Total Submissions: 184.1K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        def half(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        if head is None:
            return True
        half_head = half(head)
        reverse_half_head = reverse(half_head.next)

        same = True
        first = head
        halfp = reverse_half_head
        while same and halfp:
            if halfp.val != first.val:
                return False
            halfp = halfp.next
            first = first.next
        half_head.next = reverse(reverse_half_head)
        return same


# @lc code=end
