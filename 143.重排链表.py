#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (55.35%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    25K
# Total Submissions: 44.7K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left = 0
        pre = head

        def f(cur, right):
            nonlocal left, pre
            if not cur:
                return
            f(cur.next, right+1)
            if right > left+1:
                nextNode = pre.next
                pre.next = cur
                cur.next = nextNode
                pre = nextNode
                left += 1
            elif left+1 == right or left == right:
                cur.next = None
                left += 1
        f(head, 0)
# @lc code=end
