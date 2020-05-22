#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.61%)
# Likes:    339
# Dislikes: 0
# Total Accepted:    110.1K
# Total Submissions: 292.4K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
#
#
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
#
#
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:

        # if x <= 1:
        #     return x
        # a = 1
        # b = x
        # c = a+(b-a)//2
        # while b-a >= 2:
        #     tmp = c**2
        #     if tmp == x:
        #         return c
        #     elif tmp < x:
        #         a = c
        #         c = a+(b-a)//2
        #     else:
        #         b = c
        #         c = a+(b-a)//2
        # return c
        if x < 2:
            return x
        
        # x大于2时，平方根一定小于x/2
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right


# @lc code=end
