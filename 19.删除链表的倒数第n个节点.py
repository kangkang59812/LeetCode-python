#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (37.89%)
# Likes:    742
# Dislikes: 0
# Total Accepted:    141.3K
# Total Submissions: 370.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # points = []
        # root = ListNode(-1)
        # root.next = head
        # points.append(root)
        # while head:
        #     points.append(head)
        #     head = head.next
        # if len(points) < 2:
        #     return None

        # pre = points[-n-1]
        # cur = points[-n]
        # pre.next = cur.next
        # del cur
        # return root.next

        root = ListNode(-1)
        root.next = head
        first = root
        second = root
        for i in range(n+1):
            second = second.next
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return root.next
# @lc code=end
