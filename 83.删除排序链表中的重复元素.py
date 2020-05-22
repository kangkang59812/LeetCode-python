#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (49.37%)
# Likes:    280
# Dislikes: 0
# Total Accepted:    86.4K
# Total Submissions: 173.7K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
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
        if not head:
            return head
        s = set()
        s.add(head.val)
        pre = head
        cur = head.next
        while cur:
            if cur.next:
                if cur.val in s:
                    pre.next = cur.next
                    del cur
                    cur = pre.next

                else:

                    s.add(cur.val)
                    pre = cur
                    cur = cur.next
            else:
                if cur.val in s:
                    pre.next = None
                    del cur
                cur = None

        return head
        # @lc code=end
