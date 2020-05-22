#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (54.62%)
# Likes:    342
# Dislikes: 0
# Total Accepted:    27.4K
# Total Submissions: 50K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
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
    def pathSum(self, root: TreeNode, s: int) -> int:
        from collections import defaultdict
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1
        return self.recursionPathSum(root, prefixSumCount, s, 0)

    def recursionPathSum(self, root, prefixSumCount, s, curSum):
        if not root:
            return 0
        res = 0
        curSum += root.val

        res += prefixSumCount[curSum-s]
        prefixSumCount[curSum] = prefixSumCount[curSum]+1

        res += self.recursionPathSum(root.left, prefixSumCount, s, curSum)
        res += self.recursionPathSum(root.right, prefixSumCount, s, curSum)

        prefixSumCount[curSum] = prefixSumCount[curSum]-1
        return res
        #     res = 0
        #     if not root:
        #         return res
        #     if root.val == s:
        #         res += 1
        #     res += self.pathSum(root.left, s)
        #     res += self.pathSum(root.right, s)

        #     res += self.pathSum_root(root.left, s-root.val)
        #     res += self.pathSum_root(root.right, s-root.val)

        #     return res

        # def pathSum_root(self, root, s):
        #     if not root:
        #         return 0
        #     res = 0
        #     if root.val == s:
        #         res += 1
        #     res += self.pathSum_root(root.left, s-root.val)
        #     res += self.pathSum_root(root.right, s-root.val)
        #     return res
        # @lc code=end
