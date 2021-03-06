#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (39.16%)
# Likes:    482
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 84.5K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10
#
#

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        stack.append(-1)
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                area = max(area, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            area = max(area, heights[stack.pop()]*(len(heights)-stack[-1]-1))
        return area
        # @lc code=end
