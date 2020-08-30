#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (60.97%)
# Likes:    574
# Dislikes: 0
# Total Accepted:    84.6K
# Total Submissions: 132.7K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#
#
# 示例 1:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
#
# 示例 2:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#
#
#
#
# 说明:
#
#
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if not p:
            return q
        if not q:
            return p

        stack = [root]  # 遍历
        paths = [[root]]
        findp = False
        findq = False
        pathp = None
        pathq = None
        while stack:
            if findp and findq:
                break
            node = stack.pop()
            path = paths.pop()
            # 处理
            if node == p:
                findp = True
                pathp = path+[node]
            if node == q:
                findq = True
                pathq = path+[node]

            # 遍历
            if node.right:
                stack.append(node.right)
                paths.append(path+[node.right])
            if node.left:
                stack.append(node.left)
                paths.append(path+[node.left])

        c = None
        while True:
            if pathp[0] == pathq[0]:
                c = pathp.pop(0)
                pathq.pop(0)
            else:
                break
        return c
        # @lc code=end
