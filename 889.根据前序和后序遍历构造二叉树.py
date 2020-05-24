#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (63.17%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 7.2K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# 返回与给定的前序和后序遍历匹配的任何二叉树。
#
# pre 和 post 遍历中的值是不同的正整数。
#
#
#
# 示例：
#
# 输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
#
#
#
#
# 提示：
#
#
# 1 <= pre.length == post.length <= 30
# pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
# 每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
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
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None

        root = TreeNode(pre[0])

        # 这很重要
        if len(pre) == 1:
            return root
        mid = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:mid+2], post[:mid+1])
        root.right = self.constructFromPrePost(
            pre[mid+2:], post[mid+1:-1])
        return root

# @lc code=end
