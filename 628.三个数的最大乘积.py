#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (50.45%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    25.2K
# Total Submissions: 50K
# Testcase Example:  '[1,2,3]'
#
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#
# 示例 1:
#
#
# 输入: [1,2,3]
# 输出: 6
#
#
# 示例 2:
#
#
# 输入: [1,2,3,4]
# 输出: 24
#
#
# 注意:
#
#
# 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
#
#
#

# @lc code=start


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = float('-inf')
        res = [[-1, -2, -3], [-1, 0, 1]]
        for r in res:
            result = max(result, nums[r[0]]*nums[r[1]]*nums[r[2]])
        return result
# @lc code=end
