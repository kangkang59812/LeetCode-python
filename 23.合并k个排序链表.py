#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.30%)
# Likes:    520
# Dislikes: 0
# Total Accepted:    84K
# Total Submissions: 170.1K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # def mergeTwoLists(l1, l2):
        #     p1 = l1
        #     p2 = l2
        #     p = ListNode(-1)
        #     head = p
        #     while p1 and p2:
        #         if p1.val < p2.val:
        #             p.next = p1
        #             p1 = p1.next
        #             p = p.next
        #         else:
        #             p.next = p2
        #             p2 = p2.next
        #             p = p.next

        #     p.next = p1 if p1 else p2
        #     return head.next

        # n = len(lists)
        # if n == 0:
        #     return None

        # while n > 1:
        #     i = 0
        #     j = n-1
        #     while i < j:
        #         lists[i] = mergeTwoLists(lists[i], lists[j])
        #         del lists[j]
        #         i += 1
        #         j -= 1
        #     n = len(lists)
        # return lists[0]
        import heapq
        que = []
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(que, (node.val, index))
        newhead = ListNode(-1)
        p = newhead
        while que:
            val, index = heapq.heappop(que)
            p.next = lists[index]
            p = p.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(que, (lists[index].val, index))
        return newhead.next

# @lc code=end
