#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (38.96%)
# Likes:    319
# Dislikes: 0
# Total Accepted:    45.9K
# Total Submissions: 117.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#
# 示例 2:
#
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        count = (min(m, n)+1)//2
        res = []
        for i in range(count):
            # left->right
            for j in range(i, n-i):
                res.append(matrix[i][j])

            # top->down
            for j in range(i+1, m-i):
                res.append(matrix[j][n-1-i])

            # right->left
            for j in range(n-1-i-1, i-1, -1):
                if m-1-i != i:  # 不止一行
                    res.append(matrix[m-1-i][j])

            # bottom->top
            for j in range(m-1-i-1, i, - 1):
                if n-1-i != i:  # 不止一列
                    res.append(matrix[j][i])
        return res
        # @lc code=end
