#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (64.40%)
# Likes:    372
# Dislikes: 0
# Total Accepted:    50.3K
# Total Submissions: 77.9K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
# 返回如下的二叉树：
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(left=0, right=len(inorder)):
            nonlocal pre_idx
            if left == right:
                return None

            rootVal = preorder[pre_idx]
            root = TreeNode(rootVal)

            index = idx_map[rootVal]
            # 先左后右
            pre_idx += 1
            root.left = helper(left, index)
            root.right = helper(index+1, right)
            return root

        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()

# @lc code=end
