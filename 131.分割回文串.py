#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (68.59%)
# Likes:    344
# Dislikes: 0
# Total Accepted:    41.4K
# Total Submissions: 60.4K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#

# @lc code=start


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isHuiWen(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(s, start, length, path):
            nonlocal res
            if start == length:
                res.append(path.copy())
                return
            for i in range(start, length):
                if not isHuiWen(s, start, i):
                    continue
                path.append(s[start:i+1])
                backtrack(s, i+1, length, path)
                path.pop()

        path = []
        res = []
        backtrack(s, 0, len(s), path)
        return res
# @lc code=end
