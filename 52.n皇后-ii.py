#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (77.73%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    22.8K
# Total Submissions: 29K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
# 
# 示例:
# 
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
# [".Q..",  // 解法 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // 解法 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步，可进可退。（引用自
# 百度百科 - 皇后 ）
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        def addSolution():
            s = [['.']*n for _ in range(n)]
            for pos in queen:
                s[pos[0]][pos[1]] = 'Q'
            for i in range(n):
                s[i] = "".join(s[i])
            res.append(s)

        def placeQueen(row, col):
            queen.add((row, col))
            cols[col] = 1
            hillDia[row-col] = 1
            daleDia[row+col] = 1

        def removeQueen(row, col):
            queen.remove((row, col))
            cols[col] = 0
            hillDia[row-col] = 0
            daleDia[row+col] = 0

        def canPlace(row, col):
            return not (cols[col] + hillDia[row-col]+daleDia[row+col])

        def backtrack(row=0):
            for col in range(n):
                if canPlace(row, col):
                    placeQueen(row, col)
                    if row+1 == n:
                        addSolution()
                    else:
                        backtrack(row+1)
                    removeQueen(row, col)
        cols = [0]*n
        hillDia = [0]*(2*n-1)
        daleDia = [0]*(2*n-1)
        queen = set()
        res = []
        backtrack()
        return len(res)
# @lc code=end

