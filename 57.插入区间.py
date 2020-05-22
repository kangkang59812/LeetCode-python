#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (37.02%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 46.9K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
#
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#

# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        # if not n:
        #     return [newInterval]
        res = []
        i = 0
        new_start, new_end = newInterval
        
        while i < n and new_start > intervals[i][0]:
            res.append(intervals[i])
            i += 1

        # or res是空的 或者 res最后一个与它不交
        if not res or res[-1][1] < new_start:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], new_end)

        while i < n:
            cur = intervals[i]
            i += 1
            if res[-1][1] < cur[0]:
                res.append(cur)
            else:
                res[-1][1] = max(res[-1][1], cur[1])
        return res
        
        # @lc code=end
