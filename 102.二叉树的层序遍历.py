#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (61.08%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    97.6K
# Total Submissions: 159.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其层次遍历结果：
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 循环
        # from collections import deque
        # if not root:
        #     return []
        # que = deque()
        # que.append(root)
        # res = []
        # level = 1
        # while que:
        #     n = len(que)
        #     res.append([])

        #     for i in range(n):
        #         p = que.popleft()
        #         res[-1].append(p.val)
        #         if p.left:
        #             que.append(p.left)
        #         if p.right:
        #             que.append(p.right)
        # return res
        # 递归
        if not root:
            return []
        res = []

        def dfs(index, root):
            if len(res) < index:
                res.append([])
            res[index-1].append(root.val)

            if root.left:
                dfs(index+1, root.left)
            if root.right:
                dfs(index+1, root.right)

        dfs(1, root)
        return res
        # @lc code=end
