#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (34.70%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 46.8K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
# 例如，
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB
# ⁠   ...
#
#
# 示例 1:
#
# 输入: 1
# 输出: "A"
#
#
# 示例 2:
#
# 输入: 28
# 输出: "AB"
#
#
# 示例 3:
#
# 输入: 701
# 输出: "ZY"
#
#
#

# @lc code=start


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        x = n
        while x > 0:
            x, y = divmod(x, 26)
            if y == 0:
                y = 26
                x -= 1
            res.append(chr(64+y))
        res.reverse()
        return "".join(res)
  


# @lc code=end
