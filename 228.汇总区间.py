#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
# https://leetcode-cn.com/problems/summary-ranges/description/
#
# algorithms
# Medium (51.80%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 18.4K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
#
# 示例 1:
#
# 输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
#
# 示例 2:
#
# 输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
#
#

# @lc code=start


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            if i == len(nums)-1:
                res.append(str(nums[i]))
                break
            j = i
            end = j
            while end < len(nums)-1:
                if nums[end]+1 == nums[end+1]:
                    end += 1
                else:
                    break
            if j != end:
                res.append(str(nums[j])+"->"+str(nums[end]))
                i = end+1
            else:
                res.append(str(nums[j]))
                i = j+1

        return res
# @lc code=end
