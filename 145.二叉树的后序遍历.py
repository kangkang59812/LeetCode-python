#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (70.47%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    58.1K
# Total Submissions: 82.3K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [3,2,1]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return[]
        res = []
        stack = [root]
        # # 前序遍历逆向，入栈左右反一下即可
        # while stack:

        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)

        # return res[::-1]

        # 正常思路
        # 
        visited = set()
        while stack:
            p = stack[-1]
            while p.left and p.left not in visited:
                stack.append(p.left)
                p = p.left
            if not p.left or p.left in visited:
                if not p.right or p.right in visited:
                    stack.pop()
                    visited.add(p)
                    res.append(p.val)
                elif p.right or p.right not in visited:# 条件可不要
                    stack.append(p.right)
        return res

# @lc code=end
