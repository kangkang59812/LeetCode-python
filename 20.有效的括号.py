#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.57%)
# Likes:    1068
# Dislikes: 0
# Total Accepted:    125.2K
# Total Submissions: 315.9K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#
# 官方答案 stack and stack.pop: 先判断是否为空，然后再判断是否匹配
#                               相当于我那一大段if-else，🐂🍺

class Solution:
    def isValid(self, s: str) -> bool:
        ss = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                ss.append(s[i])
            else:
                if len(ss) == 0:
                    return False
                if s[i] == ')' and ss[-1] == '(':
                    ss.pop()
                elif s[i] == ']' and ss[-1] == '[':
                    ss.pop()
                elif s[i] == '}' and ss[-1] == '{':
                    ss.pop()
                else:
                    return False
        
        return not ss
        
