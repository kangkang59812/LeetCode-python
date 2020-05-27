#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (70.83%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 30K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
#
# 注意：
#
#
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
#
#
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for i in nums:
            x ^= i
        bit = 1
        while x & bit == 0:
            bit <<= 1
        # 两个只出现一次的数字，某些位肯定不一样，随便照这样的一位
        # 将数组按照这个规则分成两组结果
        res = [0, 0]
        for num in nums:
            if num & bit == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
# @lc code=end
