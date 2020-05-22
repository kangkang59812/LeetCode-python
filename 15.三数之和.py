#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (23.90%)
# Likes:    1738
# Dislikes: 0
# Total Accepted:    147.3K
# Total Submissions: 584.7K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        s = []
        for i in range(length):
            if nums[i] > 0:
                return s
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = length-1
            while L < R:
                if nums[i]+nums[L]+nums[R] == 0:
                    s.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif(nums[i]+nums[L]+nums[R] > 0):
                    R -= 1
                else:
                    L += 1
        return s

        # @lc code=end
