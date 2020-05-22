#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.52%)
# Likes:    736
# Dislikes: 0
# Total Accepted:    163.8K
# Total Submissions: 289.7K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
#
#
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
#


class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = 0
        xx=x
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            while x != 0:
                nums = nums*10+x % 10
                x = x//10
        if nums == xx:
            return True
        return False
