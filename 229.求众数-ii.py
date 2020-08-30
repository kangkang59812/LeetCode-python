#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (42.82%)
# Likes:    192
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 36.4K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
# 
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: [3]
# 
# 示例 2:
# 
# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        from math import floor
        c = Counter(nums)
        t = floor(len(nums)/3)
        res = []
        for k, v in dict(c).items():
            if v > t:
                res.append(k)
        return res
# @lc code=end

