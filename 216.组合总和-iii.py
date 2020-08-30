#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (70.56%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    20.8K
# Total Submissions: 29.3K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#

# @lc code=start


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(path, count, begin, rest):
            if count == 0:
                if sum(path) == n:
                    res.append(path.copy())
                    return
                else:
                    return
            for i in range(begin, 10):
                if not used[i] and i <= rest:
                    path.append(i)
                    used[i] = True
                    count -= 1
                    backtrack(path, count, i+1, rest-i)
                    path.pop()
                    used[i] = False
                    count += 1

        used = [False]*10
        path = []
        res = []
        backtrack(path, k, 1, n)
        return res
# @lc code=end
