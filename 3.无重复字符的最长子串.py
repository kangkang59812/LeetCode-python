#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.29%)
# Likes:    2376
# Dislikes: 0
# Total Accepted:    210.1K
# Total Submissions: 671.6K
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window = 0
        a = dict()
        i = 0
        j = 0
        while j < len(s):
            if s[j] in a:
                # 保证i靠右
                i = max(a[s[j]], i)
            max_window = max(max_window, j-i+1)
            a[s[j]] = j+1
            j += 1

        return max_window
# @lc code=end
