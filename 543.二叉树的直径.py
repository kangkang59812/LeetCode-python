#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (49.09%)
# Likes:    373
# Dislikes: 0
# Total Accepted:    52.6K
# Total Submissions: 104.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
# 示例 :
# 给定二叉树
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
#
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 1

        def depth(root):
            nonlocal res
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            res = max(res, r+l+1)
            return max(r, l)+1
        depth(root)
        return res-1
# @lc code=end
