#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (47.78%)
# Likes:    105
# Dislikes: 0
# Total Accepted:    21.6K
# Total Submissions: 44.9K
# Testcase Example:  '[1,3,5]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 注意数组中可能存在重复的元素。
#
# 示例 1：
#
# 输入: [1,3,5]
# 输出: 1
#
# 示例 2：
#
# 输入: [2,2,2,0,1]
# 输出: 0
#
# 说明：
#
#
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
#
#
#

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right > left:

            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[right]:
                while mid+1 < len(nums) and nums[mid + 1] == nums[mid]:
                    mid += 1
                left = mid+1
            elif nums[mid] < nums[right]:
                while mid-1 > 0 and nums[mid - 1] == nums[mid]:
                    mid -= 1
                right = mid
            else:
                right -= 1  # 不能用mid，太激进 [3,3,1,3]

        return nums[left]

# @lc code=end
