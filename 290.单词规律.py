#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (42.34%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    20.3K
# Total Submissions: 47.9K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
#
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
#
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 示例 4:
#
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
#
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
#
#

# @lc code=start


class Solution:
    def wordPattern(self, pattern: str, ss: str) -> bool:

        d = dict()
        value = set()
        patterList = [i for i in pattern]
        strList = str.split(ss)
        if len(pattern)!=len(strList):
            return False
        for p, s in zip(patterList, strList):
            if p not in d and s not in value:
                d[p] = s
                value.add(s)
            elif p not in d and s in value:
                
                return False
            else:
                if d[p] != s:
                    return False
        return True
# @lc code=end
