#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (56.77%)
# Likes:    407
# Dislikes: 0
# Total Accepted:    42.8K
# Total Submissions: 75.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
#
# 示例：
#
# 给你这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
#
#
# 说明：
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
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

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
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
        if not head or k <= 0:
            return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        n = k
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
                n = k
            else:
                break
        return dummy.next

        # @lc code=end
