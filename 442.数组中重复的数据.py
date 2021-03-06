#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#
# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (64.51%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 26.1K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
#
# 找到所有出现两次的元素。
#
# 你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
#
# 示例：
#
#
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [2,3]
#
#
#

# @lc code=start


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        # [4,3,2,7,8,2,3,1]
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1
            else:
                res.append(abs(nums[i]))
        return res
# @lc code=end
