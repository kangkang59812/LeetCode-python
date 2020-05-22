#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.74%)
# Likes:    954
# Dislikes: 0
# Total Accepted:    116.4K
# Total Submissions: 154.8K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例：
#
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
#
#
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(r, left, right):
            if len(r) == 2*n:
                res.append("".join(r))
            if left < n:
                r.append('(')
                backtrack(r, left+1, right)
                r.pop()
            if right < left:
                r.append(')')
                backtrack(r, left, right+1)
                r.pop()
        backtrack([], 0, 0)
        return res

# @lc code=end
