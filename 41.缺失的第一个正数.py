#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (36.39%)
# Likes:    400
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 102.1K
# Testcase Example:  '[1,2,0]'
#
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
#
#
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
#
#
# 说明:
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
#
#

# @lc code=start


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1
        if n == 1:
            return 2
        for i in range(n):
            # 只有存在nums[i]>len(nums)的数，则一定有一个小于len(nums)的数没有在数组中
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            a = abs(nums[i])
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])

        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n+1
    # @lc code=end
