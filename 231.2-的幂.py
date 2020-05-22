#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (47.85%)
# Likes:    176
# Dislikes: 0
# Total Accepted:    52.6K
# Total Submissions: 109.9K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        a = 2
        i = 0
        while True:
            a = 2**i
            if a == n:
                return True
            elif a > n:
                return False
            elif a < n:
                i += 1

# @lc code=end
