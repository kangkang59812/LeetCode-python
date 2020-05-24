#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (59.03%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    48.6K
# Total Submissions: 81.5K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
#
#
# 返回:
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        # def recursion(root, path, s):
        #     # 递归
        #     if not root:
        #         return
        #     s -= root.val
        #     path.append(root.val)
        #     if not root.left and not root.right and s == 0:
        #         res.append(path.copy())
        #         path.pop()
        #         return
        #     recursion(root.left, path, s)
        #     recursion(root.right, path, s)
        #     path.pop()

        # if not root:
        #     return []
        # res = []
        # recursion(root, [], s)
        # return res

        if not root:
            return []
        stack = [root]
        res = []
        paths = [[root.val]]
        while stack:
            p = stack.pop()
            path = paths.pop()
            if not p.left and not p.right and sum(path)==s:
                res.append(path.copy())
            if p.left:
                stack.append(p.left)
                paths.append(path+[p.left.val])
            if p.right:
                stack.append(p.right)
                paths.append(path+[p.right.val])
        return res
# @lc code=end
