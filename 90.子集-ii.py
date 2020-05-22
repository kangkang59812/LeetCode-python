#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (59.25%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    25.3K
# Total Submissions: 42.7K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, cur=[]):
            
            for k in range(first, n):
                if k > 0 and nums[k] == nums[k-1] and not used[k-1]:
                    continue
                cur.append(nums[k])
                res.append(cur[:])
                used[k] = True
                backtrack(k+1, cur)
                cur.pop()
                used[k] = False

        res = [[]]
        n = len(nums)
        nums.sort()
        used = [False]*n
        backtrack()
        return res
# @lc code=end
