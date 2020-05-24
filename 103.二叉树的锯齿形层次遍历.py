#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (54.03%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 89.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回锯齿形层次遍历如下：
#
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        level = 1
        res = [[]]

        while stack1:
            p = stack1.pop()
            res[-1].append(p.val)
            if level % 2 != 0:
                if p.left:
                    stack2.append(p.left)
                if p.right:
                    stack2.append(p.right)
            else:
                if p.right:
                    stack2.append(p.right)
                if p.left:
                    stack2.append(p.left)
            if not stack1:
                res.append([])
                level += 1
                stack1, stack2 = stack2, stack1
        res.pop()
        return res
# @lc code=end
