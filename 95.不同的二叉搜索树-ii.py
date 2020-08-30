#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (62.30%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 45.3K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateSubtrees(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end+1):
                lefts = generateSubtrees(start, i-1)
                rights = generateSubtrees(i+1, end)
                for l in lefts:
                    for r in rights:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        all_trees.append(cur)
            return all_trees
        return generateSubtrees(1, n) if n else []
# @lc code=end
