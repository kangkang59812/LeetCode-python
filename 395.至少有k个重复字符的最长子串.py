#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (43.89%)
# Likes:    193
# Dislikes: 0
# Total Accepted:    12.6K
# Total Submissions: 28.7K
# Testcase Example:  '"aaabb"\n3'
#
# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
#
# 示例 1:
#
#
# 输入:
# s = "aaabb", k = 3
#
# 输出:
# 3
#
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#
#
# 示例 2:
#
#
# 输入:
# s = "ababbc", k = 2
#
# 输出:
# 5
#
# 最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
#
#
#

# @lc code=start


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(x, k) for x in s.split(c))
        # @lc code=end
