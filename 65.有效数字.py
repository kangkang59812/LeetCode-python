#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#
# https://leetcode-cn.com/problems/valid-number/description/
#
# algorithms
# Hard (18.77%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    13.1K
# Total Submissions: 68.1K
# Testcase Example:  '"0"'
#
# 验证给定的字符串是否可以解释为十进制数字。
#
# 例如:
#
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：
#
#
# 数字 0-9
# 指数 - "e"
# 正/负号 - "+"/"-"
# 小数点 - "."
#
#
# 当然，在输入中，这些字符的上下文也很重要。
#
# 更新于 2015-02-10:
# C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。
#
#

# @lc code=start


class Solution:
    def isNumber(self, s: str) -> bool:
        # finals = [0, 0, 1, 0, 1, 0, 1, 0, 1]
        # transfer = [
        #     [0, 1, 2, 3, -1, -1],
        #     [-1, -1, 2, 3, -1, -1],
        #     [8, -1, 2, 4, 5, -1],
        #     [-1, -1, 4, -1, -1, -1],
        #     [8, -1, 4, -1, 5, -1],
        #     [-1, 7, 6, -1, -1, -1],
        #     [8, -1, 6, -1, -1, -1],
        #     [-1, -1, 6, -1, -1, -1],
        #     [8, -1, -1, -1, -1, -1]
        # ]
        # state = 0
        # d = {' ': 0, '+': 1, '-': 1, '.': 3, 'e': 4, 'E': 4}
        # for i in range(len(s)):
        #     if s[i] in d:
        #         reach = d[s[i]]
        #     elif s[i].isdigit():
        #         reach = 2
        #     else:
        #         reach = 5
        #     state = transfer[state][reach]
        #     if state < 0:
        #         return False
        # return bool(finals[state])
        if not s:
            return False
        numSeen, dotSeen, eSeen = False, False, False
        s = s.strip()
        for i in range(len(s)):
            if s[i].isdigit():
                numSeen = True
            elif s[i] == '.':
                # 在.之前出现.或者e，false
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            elif s[i] == 'e' or s[i] == 'E':
                if eSeen or not numSeen:
                    return False
                eSeen = True
                numSeen = False
            elif s[i] == '+' or s[i] == '-':
                if i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            else:
                return False
        return numSeen

# @lc code=end
