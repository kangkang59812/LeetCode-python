#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (54.56%)
# Likes:    563
# Dislikes: 0
# Total Accepted:    32.2K
# Total Submissions: 57K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2:
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#

# @lc code=start


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 自顶向下带备忘录
        # m = dict()

        # def dp(i, j):
        #     if (i, j) in m:
        #         return m[(i, j)]
        #     # 相当于复制没有走完的
        #     if j == -1:
        #         return i+1
        #     if i == -1:
        #         return j+1
        #     if word1[i] == word2[j]:
        #         m[(i, j)] = dp(i-1, j-1)
        #     else:

        #         m[(i, j)] = min(
        #             dp(i, j-1)+1,
        #             dp(i-1, j-1)+1,
        #             dp(i-1, j)+1
        #         )
        #     return m[(i, j)]
        # return dp(len(word1)-1, len(word2)-1)

        # 自底向上
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for j in range(1, n2+1):
            dp[0][j] = j
        for i in range(1, n1+1):
            dp[i][0] = i
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:  # word索引是从0开始的
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 增，替换，删除
                    dp[i][j] = min(
                        dp[i][j-1]+1,
                        dp[i-1][j-1]+1,
                        dp[i-1][j]+1
                    )
        return dp[-1][-1]

# @lc code=end
