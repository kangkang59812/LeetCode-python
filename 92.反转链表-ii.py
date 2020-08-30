#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (49.49%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    50.7K
# Total Submissions: 101.3K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def __init__(self):
        self.successor = None

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # nodes = []
        # p = head
        # while p:
        #     nodes.append(p)
        #     p = p.next
        #     nodes[-1].next = None
        # nodes[m-1:n] = nodes[m-1:n][::-1]
        # res = nodes[0]
        # p = nodes[0]
        # for i in range(1, len(nodes)):
        #     p.next = nodes[i]
        #     p = p.next
        # return res
        if m == 1:
            return self.reverseN(head, n)

        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last

        # @lc code=end
