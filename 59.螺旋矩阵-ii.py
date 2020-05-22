#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (76.73%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    28.2K
# Total Submissions: 36.7K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#

# @lc code=start


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        if n == 1:
            return [[1]]
        matrix = [[0]*n for _ in range(n)]
        num = 1
        m = len(matrix)
        n = len(matrix[0])
        count = (min(m, n)+1)//2

        for i in range(count):
            # left->right
            for j in range(i, n-i):
                matrix[i][j] = num
                num += 1

            # top->down
            for j in range(i+1, m-i):
                matrix[j][n-1-i] = num
                num += 1

            # right->left
            for j in range(n-1-i-1, i-1, -1):
                if m-1-i != i:  # 不止一行
                    matrix[m-1-i][j] = num
                    num += 1

            # bottom->top
            for j in range(m-1-i-1, i, - 1):
                if n-1-i != i:  # 不止一列
                    matrix[j][i] = num
                    num += 1
        return matrix
# @lc code=end
