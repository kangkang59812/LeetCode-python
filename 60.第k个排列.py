#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (48.54%)
# Likes:    241
# Dislikes: 0
# Total Accepted:    33.2K
# Total Submissions: 68.2K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
#
#
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
#
#
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"
#
#
#

# @lc code=start


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math

        def backtrack(s, length):
            if length == n:
                res.append(''.join(s))
            for i in range(1, n+1):
                if not used[i]:
                    s.append(str(i))
                    used[i] = True
                    backtrack(s, length+1)
                    s.pop()
                    used[i] = False

        total = math.factorial(n)
        numberPergroup = total//n
        start = math.ceil(k/numberPergroup)
        number = k-(start-1)*numberPergroup
        res = []
        used = [False]*(n+1)
        used[start] = True
        backtrack(s=[str(start)], length=1)
        return res[number-1]

# @lc code=end
