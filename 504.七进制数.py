#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#
# https://leetcode-cn.com/problems/base-7/description/
#
# algorithms
# Easy (48.61%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 22.3K
# Testcase Example:  '100'
#
# 给定一个整数，将其转化为7进制，并以字符串形式输出。
#
# 示例 1:
#
#
# 输入: 100
# 输出: "202"
#
#
# 示例 2:
#
#
# 输入: -7
# 输出: "-10"
#
#
# 注意: 输入范围是 [-1e7, 1e7] 。
#
#

# @lc code=start


class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = ''
        if num < 0:
            flag = '-'
        if num == 0:
            return '0'
        x = abs(num)
        res = []
        while x != 0:
            x, y = divmod(x, 7)
            res.append(str(y))
        res.reverse()
        return flag+"".join(res)
# @lc code=end
