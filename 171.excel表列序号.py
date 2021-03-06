#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#
# https://leetcode-cn.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (66.71%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    35.3K
# Total Submissions: 52.8K
# Testcase Example:  '"A"'
#
# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
# 例如，
#
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28
# ⁠   ...
#
#
# 示例 1:
#
# 输入: "A"
# 输出: 1
#
#
# 示例 2:
#
# 输入: "AB"
# 输出: 28
#
#
# 示例 3:
#
# 输入: "ZY"
# 输出: 701
#
# 致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。
#
#

# @lc code=start


class Solution:
    def titleToNumber(self, s: str) -> int:
        r = 0
        n = len(s)-1
        for i in s:
            r += (ord(i)-64)*(26**n)
            n -= 1
        return r
# @lc code=end
