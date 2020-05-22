#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (50.40%)
# Likes:    688
# Dislikes: 0
# Total Accepted:    115.2K
# Total Submissions: 227.7K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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
    def isSymmetric(self, root: TreeNode) -> bool:
        # def isMirror(p1, p2):
        #     if not p1 and not p2:
        #         return True
        #     if not p1 or not p2:
        #         return False
        #     if p1.val != p2.val:
        #         return False
        #     return isMirror(p1.left, p2.right) and isMirror(p1.right, p2.left)
        # return isMirror(root, root)

        def check(p1, p2):
            if not p1 and not p2:
                return True
            if not p1 or not p2:
                return False
            if p1.val != p2.val:
                return False
            return True
        from queue import deque
        que = deque()
        que.append((root, root))
        while que:
            p, q = que.popleft()
            if not check(p, q):
                return False
            if p:
                que.append((p.left, q.right))
                que.append((p.right, q.left))
        return True
# @lc code=end
