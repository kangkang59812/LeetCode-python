#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (40.54%)
# Likes:    309
# Dislikes: 0
# Total Accepted:    60.3K
# Total Submissions: 148.6K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#

# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] <= res[-1][-1]:
                if intervals[i][1] >= res[-1][-1]:
                    tmp = res.pop()
                    res.append([tmp[0], intervals[i][-1]])
                else:
                    continue
            else:
                res.append(intervals[i])
        return res
# @lc code=end
