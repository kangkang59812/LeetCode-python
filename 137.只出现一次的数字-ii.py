#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (66.20%)
# Likes:    332
# Dislikes: 0
# Total Accepted:    30.5K
# Total Submissions: 45.5K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,3,2]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
#
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x, y = 0, 0
        # 相当于二进制每一位操作
        # 当前位输入0，00->00,01->01,10->10
        #          1，00->01,01->10,10->00
        for num in nums:
            y = ~x & (y ^ num)
            x = ~y & (x ^ num)
        return y
# @lc code=end
