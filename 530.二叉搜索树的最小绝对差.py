#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (56.16%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 27.7K
# Testcase Example:  '[1,null,3,2]'
#
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
#
#
#
# 示例：
#
# 输入：
#
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
#
# 输出：
# 1
#
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#
#
#
#
# 提示：
#
#
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# 相同
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
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        result = float('inf')
        pre = float('inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                result = min(result, abs(root.val-pre))
                pre = root.val
                root = root.right
        return result
# @lc code=end
