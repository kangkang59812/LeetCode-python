#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (44.59%)
# Likes:    343
# Dislikes: 0
# Total Accepted:    20.6K
# Total Submissions: 46K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
#
# 输入:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# 输出: 6
#
#

# @lc code=start


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            area = 0
            stack = []
            stack.append(-1)
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                    area = max(area, heights[stack.pop()]*(i-stack[-1]-1))
                stack.append(i)
            while stack[-1] != -1:
                area = max(area, heights[stack.pop()]
                           * (len(heights)-stack[-1]-1))
            return area
        if not matrix:
            return 0
        heights = [0]*len(matrix[0])
        r_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '0':
                    heights[j] += int(matrix[i][j])
                else:
                    heights[j] = 0

            r_area = max(r_area, largestRectangleArea(heights))
        return r_area

        # @lc code=end
