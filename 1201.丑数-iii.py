#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] 丑数 III
#
# https://leetcode-cn.com/problems/ugly-number-iii/description/
#
# algorithms
# Medium (20.68%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 11.9K
# Testcase Example:  '3\n2\n3\n5'
#
# 请你帮忙设计一个程序，用来找出第 n 个丑数。
#
# 丑数是可以被 a 或 b 或 c 整除的 正整数。
#
#
#
# 示例 1：
#
# 输入：n = 3, a = 2, b = 3, c = 5
# 输出：4
# 解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
#
# 示例 2：
#
# 输入：n = 4, a = 2, b = 3, c = 4
# 输出：6
# 解释：丑数序列为 2, 3, 4, 6, 8, 9, 12... 其中第 4 个是 6。
#
#
# 示例 3：
#
# 输入：n = 5, a = 2, b = 11, c = 13
# 输出：10
# 解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
#
#
# 示例 4：
#
# 输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
# 输出：1999999984
#
#
#
#
# 提示：
#
#
# 1 <= n, a, b, c <= 10^9
# 1 <= a * b * c <= 10^18
# 本题结果在 [1, 2 * 10^9] 的范围内
#
#
#

# @lc code=start


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        from math import gcd
        # def MCM(a, b):
        #     s = a*b
        #     while b > 0:
        #         a, b = b, a % b
        #     return s/a

        def binarySearch(low, high):
            if low >= high:
                return low

            mid = low+(high-low)//2
            ab = a*b//gcd(a, b)
            ac = a*c//gcd(a, c)
            bc = b*c//gcd(b, c)
            abc = ab*c//gcd(ab, c)

            count = mid//a+mid//b+mid//c-mid//ab-mid//ac-mid//bc+mid//abc
            if count == n:
                return mid
            elif count < n:
                return binarySearch(mid+1, high)
            else:
                return binarySearch(low, mid-1)

        low = min(a, b, c)
        high = low*n
        res = binarySearch(low, high)

        return res-min(res % a, res % b, res % c)


# @lc code=end
