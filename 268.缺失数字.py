#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#
# https://leetcode-cn.com/problems/missing-number/description/
#
# algorithms
# Easy (54.88%)
# Likes:    238
# Dislikes: 0
# Total Accepted:    57.2K
# Total Submissions: 104.2K
# Testcase Example:  '[3,0,1]'
#
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#
# 示例 1:
#
# 输入: [3,0,1]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
#
#
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
#
#

# @lc code=start


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        i = 0
        while i < len(nums)+1:
            a ^= i
            i += 1
        i = 0
        while i < len(nums):
            a ^= nums[i]
            i += 1
        return a
# @lc code=end
