#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (64.70%)
# Likes:    431
# Dislikes: 0
# Total Accepted:    80.9K
# Total Submissions: 125K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def reverse(head: ListNode)-> ListNode:
            pre = None
            cur = head
            tmp = None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        n = 2
        while p.next:
            tmp = p
            while tmp and tmp.next and n > 0:
                tmp = tmp.next
                n -= 1
            if n == 0:
                next_node = tmp.next
                tail = p.next
                # 翻转k个节点
                tmp.next = None
                p.next = reverse(tail)
                tail.next = next_node
                p = tail
                n = 2
            else:
                break
        return dummy.next
        # @lc code=end
