#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (39.37%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    10.6K
# Total Submissions: 26.9K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]'
#
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
# 示例:
#
# 输入:
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
#
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
#
# 提示:
#
#
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
# 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
#
#
#

# @lc code=start


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
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

        res = []
        for word in words:
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
                    break
            if flag:
                res.append(word)

        return res
# @lc code=end
