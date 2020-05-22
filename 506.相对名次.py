#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
# https://leetcode-cn.com/problems/relative-ranks/description/
#
# algorithms
# Easy (53.78%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 15.6K
# Testcase Example:  '[5,4,3,2,1]'
#
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold
# Medal", "Silver Medal", "Bronze Medal"）。
#
# (注：分数越高的选手，排名越靠前。)
#
# 示例 1:
#
#
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and
# "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
#
# 提示:
#
#
# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。
#
#
#

# @lc code=start


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        s = nums[::]
        s.sort(reverse=True)
        res = [' ']*len(nums)
        if len(nums) == 0:
            return []
        res[nums.index(s[0])] = "Gold Medal"
        if len(nums) == 1:
            return [res[0]]
        res[nums.index(s[1])] = "Silver Medal"
        if len(nums) == 2:
            return res[:2]
        res[nums.index(s[2])] = "Bronze Medal"
        if len(nums) == 3:
            return res

        for i in range(len(s)):
            if res[i] == ' ':
                res[i] = str(s.index(nums[i])+1)
        return res
# @lc code=end
