#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (44.18%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    11.1K
# Total Submissions: 25.1K
# Testcase Example:  '[1,null,2,2]'
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#
# 假定 BST 有如下定义：
#
#
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
#
#
# 例如：
# 给定 BST [1,null,2,2],
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
#
#
# 返回[2].
#
# 提示：如果众数超过1个，不需考虑输出顺序
#
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
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
    def findMode(self, root: TreeNode) -> List[int]:
        from collections import Counter
        if not root:
            return []

        def middleOrder(root):
            if not root:
                return []
            return middleOrder(root.left)+[root.val]+middleOrder(root.right)
        res = []
        count = Counter(middleOrder(root))
        max_count = count.most_common(1)[0][1]
        for k in count.most_common():
            if k[1] == max_count:
                res.append(k[0])
            else:
                break
        return res


# @lc code=end
