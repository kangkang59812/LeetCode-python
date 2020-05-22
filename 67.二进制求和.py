#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (50.47%)
# Likes:    277
# Dislikes: 0
# Total Accepted:    54.1K
# Total Submissions: 104.9K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#

# @lc code=start


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)
        if n1 < n2:
            a, b = b, a
            n1, n2 = n2, n1
        i = n1-1
        j = n2-1
        c = 0
        s = []
        while i > -1 and j > -1:
            x, y = divmod((int(a[i])+int(b[j])+c), 2)
            y = str(y)
            s.append(y)
            c = x
            i -= 1
            j -= 1
        if j < 0:
            for t in range(i, -1, -1):
                x, y = divmod((int(a[t])+c), 2)
                y = str(y)
                s.append(y)
                c = x

        if c == 1:
            s.append('1')
        return "".join(s[::-1])


# @lc code=end
