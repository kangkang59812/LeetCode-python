#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (37.58%)
# Likes:    329
# Dislikes: 0
# Total Accepted:    66.3K
# Total Submissions: 169.7K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstIndex, lastIndex = -1, -1

        # 左边界
        low, high = 0, len(nums)-1
        while low <= high:
            middle = (low+high)//2  # low + (high-low)//2
            if nums[middle] == target:
                high = middle-1
            elif target > nums[middle]:
                low = middle+1
            elif target < nums[middle]:
                high = middle-1
        if low >= len(nums) or target != nums[low]:
            return [firstIndex, lastIndex]
        firstIndex = low

        # 右边界
        low, high = 0, len(nums)-1
        while low <= high:
            middle = (low+high)//2  # low + (high-low)//2
            if nums[middle] == target:
                low = middle+1
            elif target > nums[middle]:
                low = middle+1
            elif target < nums[middle]:
                high = middle-1

        if high < 0 or target != nums[high]:
            return [-1, -1]

        lastIndex = high

        return [firstIndex, lastIndex]

        # @lc code=end
