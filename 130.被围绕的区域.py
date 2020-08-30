#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (42.14%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    69.2K
# Total Submissions: 163.8K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# 解释:
#
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#

# @lc code=start


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != "O":
                return
            direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            board[x][y] = "Y"
            for d in direction:
                dfs(x+d[0], y+d[1])

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(1, n-1):
            dfs(0, i)
            dfs(m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"
# @lc code=end
