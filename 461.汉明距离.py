#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#
# https://leetcode-cn.com/problems/hamming-distance/description/
#
# algorithms
# Easy (75.46%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 64.5K
# Testcase Example:  '1\n4'
#
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 2^31.
#
# 示例:
#
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。
#
#
#

# @lc code=start


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #右移，n=n^n-1, count++直到n=0
        s = bin(x ^ y)[2:]

        return sum([int(i) for i in s if i == '1'])
        # xor = x ^ y
        # distance = 0
        # while xor:
        #     distance += 1
        #     # remove the rightmost bit of '1'
        #     xor = xor & (xor - 1)
        # return distance
# @lc code=end
