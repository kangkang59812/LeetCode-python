#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
# https://leetcode-cn.com/problems/island-perimeter/description/
#
# algorithms
# Easy (65.91%)
# Likes:    173
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 22.8K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
#
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
#
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
# 。计算这个岛屿的周长。
#
#
#
# 示例 :
#
# 输入:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
#
# 输出: 16
#
# 解释: 它的周长是下面图片中的 16 个黄色的边：
#
#
#
#
#

# @lc code=start


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        # r = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             for bias_x, bias_y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        #                 x, y = i+bias_x, j+bias_y
        #                 if (x == -1 or y == -1 or x == m or y == n) or grid[x][y] == 0:
        #                     r += 1
        # return r

        # DFS搜索法

        def dfs(grid, x, y):
            if not(0 <= x < len(grid) and 0 <= y < len(grid[0])):
                return 1
            if grid[x][y] == 0:
                return 1
            if grid[x][y] != 1:
                return 0

            grid[x][y] = 2
            return dfs(grid, x+1, y)+dfs(grid, x-1, y)+dfs(grid, x, y+1)+dfs(grid, x, y-1)

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
        return 0
# @lc code=end
