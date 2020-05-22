#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (31.94%)
# Likes:    398
# Dislikes: 0
# Total Accepted:    44.6K
# Total Submissions: 135.5K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#

# @lc code=start


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return
        i, k = len(nums)-2, len(nums)-1
        while i >= 0 and nums[i] >= nums[i-1]:
            i = i-1

        if i >= 0:
            while k >= 0 and nums[i] >= nums[k]:
                k = k-1
            nums[i], nums[k] = nums[k], nums[i]
        p = i+1
        q = len(nums)-1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1

            # @lc code=end
