#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
# https://leetcode-cn.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (52.59%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    15.5K
# Total Submissions: 29.1K
# Testcase Example:  '"abcdefg"\n2'
#
# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
#
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
#
#
#
#
# 示例:
#
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#
#
#
#
# 提示：
#
#
# 该字符串只包含小写英文字母。
# 给定字符串的长度和 k 在 [1, 10000] 范围内。
#
#
#

# @lc code=start


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k >= len(s):
            return s[::-1]
        if k <= len(s) <= 2*k:
            return s[:k][::-1]+s[k:]
        res = ""
        i = 0
        j = 2*k-1
        while j <= len(s)-1:
            res += s[i:i+k][::-1]+s[i+k:j+1]
            i = i+2*k
            j = j+2*k
        residue = s[i:]
        if k >= len(residue):
            return res+residue[::-1]
        if k <= len(residue) <= 2*k:
            return res+residue[:k][::-1]+residue[k:]
        return res
        # @lc code=end
