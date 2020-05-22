#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (35.91%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    30.9K
# Total Submissions: 86.1K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#

# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = list()
        p = 0
        n = len(nums)
        while p < n-3:
            if nums[p] + nums[p+1]*3 > target:
                break
            if nums[p] + 3*nums[-1] < target:
                while p < n-4 and nums[p] == nums[p+1]:
                    p += 1
                p += 1  # 当前的nums[p] + 3*nums[-1]仍然小于target，所以+1
                continue
            k = p+1
            while k < n-2:
                if nums[k] + nums[k+1]*2 > target-nums[p]:
                    break
                if nums[k] + 2*nums[-1] < target-nums[p]:
                    while k < n-3 and nums[k] == nums[k+1]:
                        k += 1
                    k += 1
                    continue
                i = k+1
                j = n-1
                while i < j:
                    t = nums[p]+nums[k]+nums[i]+nums[j]
                    if t == target:
                        result.append([nums[p], nums[k], nums[i], nums[j]])

                        while i < j and nums[i] == nums[i+1]:
                            i += 1
                        while i < j and nums[j] == nums[j-1]:
                            j -= 1
                        i += 1
                        j -= 1
                    elif t > target:
                        j -= 1
                    else:
                        i += 1

                while k < n-3 and nums[k] == nums[k+1]:
                    k += 1
                k += 1
            while p < n-4 and nums[p] == nums[p+1]:
                p += 1
            p += 1

        return result


# @lc code=end
