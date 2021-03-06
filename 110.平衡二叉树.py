#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (50.63%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    62.3K
# Total Submissions: 122.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回 true 。
#
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# 返回 false 。
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
    def helper(self, root):
        if not root:
            return True, 0

        leftIs, leftHeigth = self.helper(root.left)
        if leftIs is False:
            return False, -1

        rightIs, rightHeight = self.helper(root.right)
        if rightIs is False:
            return False, -1

        return (abs(leftHeigth-rightHeight) < 2,
                1+max(leftHeigth, rightHeight))

    def isBalanced(self, root: TreeNode) -> bool:

        # return self.helper(root)[0]

        # 后序遍历
        if not root:
            return True
        res = {None: (True, 0)}
        stack = [root]
        visited = set()
        while stack:
            p = stack[-1]
            leftVisited = True
            rightVisited = True
            if p.right and p.right not in visited:
                rightVisited = False
                stack.append(p.right)
            if p.left and p.left not in visited:
                leftVisited = False
                stack.append(p.left)
            if leftVisited and rightVisited:
                if abs(res[p.left][1]-res[p.right][1]) <= 1:
                    res[p] = (True,
                              max(res[p.left][1], res[p.right][1])+1)
                    visited.add(p)
                    stack.pop()
                else:
                    return False

        return res[root][0]

        # @lc code=end
