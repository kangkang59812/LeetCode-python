#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
# https://leetcode-cn.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (23.01%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 59.4K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# 给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n
# 也是一个整数。
#
# 示例 1:
#
# 输入: [23,2,4,6,7], k = 6
# 输出: True
# 解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
#
#
# 示例 2:
#
# 输入: [23,2,6,4,7], k = 6
# 输出: True
# 解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
#
#
# 说明:
#
#
# 数组的长度不会超过10,000。
# 你可以认为所有数字总和在 32 位有符号整数范围内。
#
#
#

# @lc code=start


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        s = 0
        d = dict()
        d[0] = -1  # 特判连续的0
        for i in range(len(nums)):
            s += nums[i]
            if k != 0:
                s %= k
            if s in d:
                if i-d[s] > 1:
                    return True
            else:
                d[s] = i
        return False
# @lc code=end
