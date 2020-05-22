#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.74%)
# Likes:    703
# Dislikes: 0
# Total Accepted:    123.4K
# Total Submissions: 354.3K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#
# 最佳答案用zip提取每个元素的各个位置，然后判断是否重复


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        m = min(list(map(len, strs)))
        c = ''
        for i in range(m):
            ch = [s[i] for s in strs]
            if min(ch) == max(ch):
                c += ch[0]
            else:
                break
        return c
