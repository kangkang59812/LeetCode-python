#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (68.83%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    24.4K
# Total Submissions: 35.1K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 我们应返回其最大深度，3。
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # res = 0

        # def depth(root):
        #     nonlocal res
        #     if not root:
        #         return 0
        #     m = 0
        #     for c in root.children:
        #         m = max(depth(c), m)
        #     res = max(m+1, res)
        #     return m+1
        # depth(root)
        # return res

        from collections import deque
        if not root:
            return 0
        que = deque()
        que.append(root)
        level = 0
        while que:
            n = len(que)
            level += 1
            for i in range(n):     
                p = que.popleft()
                if p.children:
                    for c in p.children:
                        que.append(c)
        return level
        # @lc code=end
