#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (37.59%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    35K
# Total Submissions: 93K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
#
# 示例 1:
#
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
#
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row*col-1
        while left <= right:
            middle = left+(right-left)//2
            num = matrix[middle//col][middle % col]
            if num > target:
                right = middle-1
            elif num < target:
                left = middle + 1
            elif num == target:
                return True
        return False
    


# @lc code=end
