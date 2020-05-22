#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (37.06%)
# Likes:    247
# Dislikes: 0
# Total Accepted:    31.1K
# Total Submissions: 82.7K
# Testcase Example:  '[2,3,2]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
#
# 示例 2:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        def line_rob(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 2 or n == 1:
                return max(nums)
            dp = [[0] for _ in range(n+1)]
            dp[0] = 0
            dp[1] = nums[0]
            #或者用dp[n] = MAX( dp[n-1], dp[n-2] + num )
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            return dp[n]

        if len(nums) == 1:
            return nums[0]
        # 第一家偷或者不偷，分成两种情况，取最大
        return max(line_rob(nums[:-1]), line_rob(nums[1:]))

# @lc code=end
