#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (60.18%)
# Likes:    541
# Dislikes: 0
# Total Accepted:    126.7K
# Total Submissions: 210.5K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明:
#
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
#
#

# @lc code=start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # from collections import deque
        # queue = deque()
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         queue.append(i)
        #     elif len(queue) != 0 and queue[0] == i:
        #         break
        #     else:
        #         if len(queue) != 0:
        #             j = queue.popleft()
        #             queue.append(i)
        #             nums[i], nums[j] = nums[j], nums[i]
        #         else:
        #             continue
        l = r = 0
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l += 1
            r += 1

# @lc code=end
