#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (76.73%)
# Likes:    492
# Dislikes: 0
# Total Accepted:    69.2K
# Total Submissions: 90K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, cur=[]):
     
            for k in range(first, n):
                cur.append(nums[k])
                res.append(cur[:])
                backtrack(k+1, cur)
                cur.pop()
        res = [[]]
        n = len(nums)
       
        backtrack()
        return res
# @lc code=end
