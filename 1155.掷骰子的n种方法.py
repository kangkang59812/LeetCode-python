#
# @lc app=leetcode.cn id=1155 lang=python3
#
# [1155] 掷骰子的N种方法
#
# https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (42.99%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 8.6K
# Testcase Example:  '1\n6\n3'
#
# 这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。
#
# 我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。
#
# 如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10^9 + 7 后返回。
#
#
#
# 示例 1：
#
# 输入：d = 1, f = 6, target = 3
# 输出：1
#
#
# 示例 2：
#
# 输入：d = 2, f = 6, target = 7
# 输出：6
#
#
# 示例 3：
#
# 输入：d = 2, f = 5, target = 10
# 输出：1
#
#
# 示例 4：
#
# 输入：d = 1, f = 2, target = 3
# 输出：0
#
#
# 示例 5：
#
# 输入：d = 30, f = 30, target = 500
# 输出：222616187
#
#
#
# 提示：
#
#
# 1 <= d, f <= 30
# 1 <= target <= 1000
#
#
#

# @lc code=start


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d*f:
            return 0
        if d == 1:
            return 1
        pre = [0 for i in range(f*d+1)]
        cur = [0 for i in range(f*d+1)]
        for i in range(1, f+1):
            pre[i] = 1
        for i in range(2, d+1):
            for j in range(i, f*i+1):
                for k in range(1, min(j+1, f+1)):
                    cur[j] += pre[j-k]
            pre, cur = cur, [0 for i in range(f*d+1)]

        return pre[target] % (10**9+7)
# @lc code=end
