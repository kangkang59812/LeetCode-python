#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (46.59%)
# Likes:    6293
# Dislikes: 0
# Total Accepted:    555.9K
# Total Submissions: 1.2M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}  # 保存已经遍历
        for i, one in enumerate(nums):
            result = target-one
            if result not in d:
                if one in d:  # [3,3,1,6] 9这种，test里是按[0,3]算的；不加这个就是[1,3]
                    continue
                d[one] = i  # 保存已经遍历过的数和下标
            else:
                return [d[result], i]  # 如果result在字典里，返回它的下标和当前数的下标
