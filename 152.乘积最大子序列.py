#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (37.44%)
# Likes:    421
# Dislikes: 0
# Total Accepted:    41.2K
# Total Submissions: 109.5K
# Testcase Example:  '[2,3,-2,4]'
#
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
#

# @lc code=start


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = float('-inf')
        imax = 1
        imin = 1
        for i in range(n):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax*nums[i], nums[i])
            imin = min(imin*nums[i], nums[i])
            max_value = max(max_value, imax)
        return max_value

        # @lc code=end
