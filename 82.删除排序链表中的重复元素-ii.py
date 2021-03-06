#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (46.99%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    45.9K
# Total Submissions: 96.3K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = ListNode(None)
        newhead.next = head
        p1 = newhead
        p2 = head
        repeat = 0
        while p1.next:
            while p2.next and p1.next.val == p2.next.val:
                p2 = p2.next
                repeat = 1
            if repeat:
                p1.next = p2.next
                p2 = p2.next
                repeat = 0
            else:
                p1 = p2
                if p2:
                    p2 = p2.next

        return newhead.next
# @lc code=end
