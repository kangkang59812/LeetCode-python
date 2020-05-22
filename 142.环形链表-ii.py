#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (49.51%)
# Likes:    469
# Dislikes: 0
# Total Accepted:    77.2K
# Total Submissions: 153.6K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
# 说明：不允许修改给定的链表。
#
#
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
# 示例 2：
#
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
# 示例 3：
#
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#
#
#
#
#
#
# 进阶：
# 你是否可以不用额外空间解决此题？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 得到环的长度
        if head is None or head.next is None:
            return None
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
        index = slow
        count = 1
        slow = slow.next
        while slow != fast:
            slow = slow.next
            count += 1

        # 相遇正好差一个环的长度
        p1 = head
        p2 = head
        for i in range(count):
            p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
# @lc code=end
