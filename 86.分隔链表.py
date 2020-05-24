#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (56.70%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    36.9K
# Total Submissions: 64K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        nodes = []
        index1 = []
        index2 = []
        p = head
        count = 0
        while p:
            if p.val < x:
                index1.append(count)
            else:
                index2.append(count)
            count += 1
            nodes.append(p)
            p = p.next
            nodes[-1].next = None
        start = 0
        i = 0
        if len(index1) > 0:
            i = 1
            start = index1[0]
        p = nodes[start]
        while len(index1) > 0 and i < len(index1):
            nodes[start].next = nodes[index1[i]]
            nodes[start] = nodes[start].next
            i += 1

        i = 0
        if len(index1) < 1:
            i = 1
            start = index2[0]
        while len(index2) > 0 and i < len(index2):
            nodes[start].next = nodes[index2[i]]
            nodes[start] = nodes[start].next
            i += 1
        return p
        # @lc code=end
