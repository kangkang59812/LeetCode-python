#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.25%)
# Likes:    312
# Dislikes: 0
# Total Accepted:    37.4K
# Total Submissions: 160.7K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#
#
# 示例 2:
#
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#
#

# @lc code=start


class Solution:
    def numDecodings(self, s: str) -> int:
        # 递归超时
        # def decode(s, index):
        #     if s[0] == '0':
        #         return 0
        #     if index <= 0:
        #         return 1

        #     count = 0
        #     cur = s[index]
        #     pre = s[index-1]

        #     if cur > '0':
        #         count = decode(s, index-1)
        #     if pre == '1' or (pre == '2' and cur <= '6'):
        #         count += decode(s, index-2)

        #     return count

        # return decode(s, len(s)-1)
        if s[0] == '0':
            return 0
        pre, cur = 1, 1  # dp[-1] dp[0]
        dp = [0]*(len(s)+1)
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            #tmp = cur
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    #cur = pre
                    #s[i-1] s[i] 被唯一编码为10 或者 20
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] >= '1' and s[i] <= '6'):
                #cur = cur+pre
                #          s[i+1]与s[i]分开+合体编码
                dp[i+1] = dp[i]+dp[i-1]
            else:
                dp[i+1] = dp[i]
            #pre = tmp
        return dp[len(s)]

        # @lc code=end
