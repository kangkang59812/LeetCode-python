#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (49.74%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 57.3K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
#
#
#

# @lc code=start


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1)-1, len(num2)-1
        res = []
        if n < m:
            num1, num2 = num2, num1
            n, m = m, n
        carreir = 0
        while n > -1 and m > -1:
            x, y = divmod(int(num1[n])+int(num2[m])+carreir, 10)
            res.append(str(y))
            carreir = x
            m -= 1
            n -= 1
        while n > -1:
            x, y = divmod(int(num1[n])+carreir, 10)
            res.append(str(y))
            carreir = x
            n -= 1
        if carreir:
            res.append('1')
        res.reverse()
        return "".join(res)
# @lc code=end
