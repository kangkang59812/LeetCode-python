#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (48.32%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    21.8K
# Total Submissions: 45K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
#
#
# 示例 2:
#
# 输入: 5
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#

# @lc code=start


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # if num <= 0:
        #     return False
        # s = bin(num)[2:]
        # index = len(s)

        # return num & (num-1) == 0 and index % 2 == 1
        # 这种判断等效于和010101.。。。与
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0
# @lc code=end
