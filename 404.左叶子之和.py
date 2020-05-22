#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (54.27%)
# Likes:    138
# Dislikes: 0
# Total Accepted:    20.3K
# Total Submissions: 37.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def leftNum(root, res):
            if not root:
                return
           
            if root.left is not None and root.left.left is None and root.left.right is None:
                res.append(root.left.val)
            
            leftNum(root.left, res)
            leftNum(root.right, res)
        res = []
        leftNum(root, res)
        return sum(res)
# @lc code=end
