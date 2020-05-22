#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (40.88%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    43.6K
# Total Submissions: 106.6K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
#
# 提示：
#
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
#

# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(pos, length):
            nonlocal flag
            if flag:
                return
            if length == len(word):
                flag = True
                return
            for mo in move:
                x = pos[0]+mo[0]
                y = pos[1]+mo[1]
                if -1 < x < n and -1 < y < m:
                    if board[y][x] == word[length] and not used[y][x]:
                        used[y][x] = True
                        backtrack([x, y], length+1)
                        used[y][x] = False
                        if flag:
                            return

        flag = False
        move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m, n = len(board), len(board[0])
        used = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    backtrack([j, i], 1)
                    used[i][j] = False
                    if flag:
                        return flag
        return flag


# @lc code=end
