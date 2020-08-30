#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (41.98%)
# Likes:    322
# Dislikes: 0
# Total Accepted:    57.9K
# Total Submissions: 137.5K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明：
#
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#
#

# @lc code=start


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0]*(m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                sums = mul+res[i+j+1]
                res[i+j+1] = sums % 10
                res[i+j] = res[i+j]+sums//10
        cur = 0
        while cur < len(res) and res[cur] == 0:
            cur = cur+1
        # 去除前导0
        resultstring = ''
        for i in range(cur, len(res)):
            resultstring = resultstring+(str)(res[i])
        if resultstring == '':
            return '0'
        return resultstring

# @lc code=end
