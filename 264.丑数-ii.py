#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (50.90%)
# Likes:    264
# Dislikes: 0
# Total Accepted:    23.4K
# Total Submissions: 45.6K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
# 说明:  
#
#
# 1 是丑数。
# n 不超过1690。
#
#
#

# @lc code=start


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        nums = [1]
        for i in range(n-1):
            ugly = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            nums.append(ugly)

            # 避免重复
            if ugly == nums[i2]*2:
                i2 += 1
            if ugly == nums[i3]*3:
                i3 += 1
            if ugly == nums[i5]*5:
                i5 += 1
        return nums[-1]


# @lc code=end
