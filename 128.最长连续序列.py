#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (48.16%)
# Likes:    270
# Dislikes: 0
# Total Accepted:    30.8K
# Total Submissions: 63.8K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 
# 要求算法的时间复杂度为 O(n)。
# 
# 示例:
# 
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        if not snums:
            return 0
        res = 1
        for num in snums:
            if num-1 not in snums:
                cur = num
                count = 1
                while cur+1 in snums:
                    cur = cur+1
                    count += 1

                res = max(res, count)
        return res
        
# @lc code=end

