#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# https://leetcode-cn.com/problems/keyboard-row/description/
#
# algorithms
# Easy (68.53%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 22.8K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
#
#
#
#
#
#
#
# 示例：
#
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
#
#
#
#
# 注意：
#
#
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。
#
#

# @lc code=start


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def AllinRow(word):
            row1 = 'qwertyuiop'
            row2 = 'asdfghjkl'
            row3 = 'zxcvbnm'
            row = [row1, row2, row3]
            for r in row:
                allin = 1
                for c in word:
                    if c not in r:
                        allin = 0
                        break
                if allin:
                    return word

        res = []
        for word in words:
            r = AllinRow(word.lower())
            if r:
                res.append(word)
        return res

# @lc code=end
