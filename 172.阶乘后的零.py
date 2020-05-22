#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (39.89%)
# Likes:    256
# Dislikes: 0
# Total Accepted:    32K
# Total Submissions: 80.2K
# Testcase Example:  '3'
#
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例 1:
#
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
# 示例 2:
#
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
#
# 说明: 你算法的时间复杂度应为 O(log n) 。
#
#

# @lc code=start


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
       
        while n > 0:
            
            count += int(n//5)
            n /= 5 # 5 的个数就是 n / 5 + n / 25 + n / 125
           
        return count
# @lc code=end
