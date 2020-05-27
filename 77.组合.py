#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (73.42%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    51.1K
# Total Submissions: 69.4K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(begin, res, path):
            if len(path) == k:
                res.append(path.copy())
            for i in range(begin, n+1):
                path.append(i)
                backtrack(i+1, res, path)
                path.pop()
                
        res = []
        path = []
        backtrack(1, res, path)
        return res
# @lc code=end
