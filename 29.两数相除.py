#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (19.42%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    43.1K
# Total Submissions: 220.8K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
# -2
#
#
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
#
# 示例 2:
#
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
#
#
#
# 提示：
#
#
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
#
#
#

# @lc code=start


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            divisor <<= 1
            count += 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count
                dividend -= divisor
        if sign:
            result = -result
        return result if -(1 << 31) <= result <= (1 << 31)-1 else (1 << 31)-1
# @lc code=end
