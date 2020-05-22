#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (32.99%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    50.1K
# Total Submissions: 151.8K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
#

# @lc code=start


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        isPrim = [True]*(n+1)
        isPrim[0] = False
        isPrim[1] = False
        isPrim[-1] = False
        i = 2
        while i**2 < n:

            if isPrim[i]:
                j = i**2
                while j < n:
                    isPrim[j] = False
                    j += i
            i += 1
        return sum(isPrim)
# @lc code=end
