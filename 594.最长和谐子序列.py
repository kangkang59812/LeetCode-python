#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#
# https://leetcode-cn.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (48.25%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    14.9K
# Total Submissions: 30.8K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
# 
# 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
# 
# 示例 1:
# 
# 
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
# 
# 
# 说明: 输入的数组长度最大不超过20,000.
# 
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        c = dict(Counter(nums))
        res = 0
        for k, v in c.items():
            if k+1 in c:
                res = max(res, c[k]+c[k+1])
            if k-1 in c:
                res = max(res, c[k]+c[k-1])
        return res
# @lc code=end

