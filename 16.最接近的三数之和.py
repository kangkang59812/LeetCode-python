#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.65%)
# Likes:    346
# Dislikes: 0
# Total Accepted:    68.4K
# Total Submissions: 160.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#

# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        L = 0
        R = len(nums)-1
        if len(nums) == 0:
            return None
        close = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            L = i+1
            R = len(nums)-1
            while(L < R):
                s = (nums[L] + nums[R] + nums[i])
                if abs(target-s) < abs(target-close):
                    close = s

                if s > target:
                    R = R-1
                elif s < target:
                    L = L+1
                else:
                    return close
        return close

# @lc code=end
