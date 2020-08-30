#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (41.83%)
# Likes:    261
# Dislikes: 0
# Total Accepted:    41.7K
# Total Submissions: 98.7K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s
# 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
#
# 示例: 
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#
#
# 进阶:
#
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#

# @lc code=start


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        window = []
        ss = 0
        res = len(nums)+1
        i = 0
        for j in range(len(nums)):
            ss += nums[j]
            while ss >= s:
                res = min(res, j-i+1)
                ss -= nums[i]
                i += 1
        return res if res!=(len(nums)+1) else 0
                
            # @lc code=end
