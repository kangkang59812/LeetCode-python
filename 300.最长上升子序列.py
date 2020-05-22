#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.23%)
# Likes:    447
# Dislikes: 0
# Total Accepted:    54.5K
# Total Submissions: 123.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#

# @lc code=start


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划
        # if len(nums) = 0:
        #     return 0
        # dp = [1]*len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], 1+dp[j])
        # return max(dp)

        # 动态+二分
        if len(nums) < 2:
            return len(nums)
        cell = [nums[0]]
        for num in nums[1:]:
            if num > cell[-1]:
                cell.append(num)
                continue
            #用它覆盖掉比它大的元素中最小的那个
            left, right = 0, len(cell)-1
            while left < right:
                middle = left+(right-left)//2
                if cell[middle] > num:
                    right = middle
                elif cell[middle] < num:
                    left = middle+1
                elif cell[middle] == num:
                    right = middle
            cell[left] = num

        return len(cell)

            # @lc code=end
