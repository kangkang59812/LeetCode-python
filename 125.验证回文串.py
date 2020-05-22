#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (42.74%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    91K
# Total Submissions: 211.3K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
#
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def not_letter_digit(c):
            return not 'A' <= c <= 'Z' and not 'a' <= c <= 'z' and not '0' <= c <= '9'
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not_letter_digit(s[left]):
                left += 1
            while left < right and not_letter_digit(s[right]):
                right -= 1
            sl = str.lower(s[left])
            sr = str.lower(s[right])
            if sl != sr:
                return False
            left += 1
            right -= 1
        return True
        # @lc code=end
