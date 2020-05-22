#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (44.83%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    68.4K
# Total Submissions: 152.5K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 加个头结点
        p = ListNode(-1)
        p.next = head
        pre = p
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                del cur
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return p.next
# @lc code=end
