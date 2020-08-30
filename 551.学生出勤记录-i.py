#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#
# https://leetcode-cn.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (51.02%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 29.6K
# Testcase Example:  '"PPALLP"'
#
# 给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
#
#
# 'A' : Absent，缺勤
# 'L' : Late，迟到
# 'P' : Present，到场
#
#
# 如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
#
# 你需要根据这个学生的出勤记录判断他是否会被奖赏。
#
# 示例 1:
#
# 输入: "PPALLP"
# 输出: True
#
#
# 示例 2:
#
# 输入: "PPALLL"
# 输出: False
#
#
#

# @lc code=start


class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = 0
        for i in range(len(s)):
            if s[i] == 'A':
                A += 1
            if A > 1:
                return False
        for i in range(len(s)-2):
            if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                L += 1

            if L > 0:
                return False
        return True
        
        # @lc code=end
