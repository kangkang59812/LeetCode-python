#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (74.57%)
# Likes:    711
# Dislikes: 0
# Total Accepted:    128.2K
# Total Submissions: 168.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # def backtrack(begin, n, path, res):
        #     if len(path) == n:
        #         res.append(path.copy())
        #         return
        #     for i in range(begin, n):
        #         nums[i], nums[begin] = nums[begin], nums[i]
        #         path.append(nums[begin])
        #         backtrack(begin+1, n, path, res)
        #         path.pop()
        #         nums[begin], nums[i] = nums[i], nums[begin]
        # res = []
        # path = []
        # n = len(nums)
        # backtrack(0, n, path, res)
        # return res
        from itertools import permutations
        return list(permutations(nums, len(nums)))
# @lc code=end
