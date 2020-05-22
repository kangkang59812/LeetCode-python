#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (66.79%)
# Likes:    547
# Dislikes: 0
# Total Accepted:    67.4K
# Total Submissions: 98.4K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, n, path, res, target):
            if target == 0:
                res.append(path.copy())
                return
            for i in range(begin, n):
                residue = target-candidates[i]
                if residue < 0:
                    break
                path.append(candidates[i])
                dfs(candidates, i, n, path, res, residue)
                path.pop()

        n = len(candidates)
        if n == 0:
            return []
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, n, path, res, target)
        return res


# @lc code=end
