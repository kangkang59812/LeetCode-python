#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (49.56%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    29.6K
# Total Submissions: 59.8K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
#
#
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
#
# 说明:
# 元音字母不包含字母"y"。
#
#

# @lc code=start


class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 0:
            return ""
        left, right = 0, len(s)-1
        a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = [""]*(right+1)
        while left < right:
            if s[left] in a and s[right] in a:
                res[left] = s[right]
                res[right] = s[left]
                left += 1
                right -= 1
                continue
            elif s[left] in a:
                res[right] = s[right]
                right -= 1
            elif s[right] in a:
                res[left] = s[left]
                left += 1
            else:
                res[left] = s[left]
                res[right] = s[right]
                left += 1
                right -= 1
        if res[left] == "":
            res[left] = s[left]
        return "".join(res)
        # @lc code=end
