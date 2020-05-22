#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (61.42%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    91.3K
# Total Submissions: 148.4K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#

# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r):
            i = l-1
            tmp = nums[r]
            # i+1指向的是要被替换的位置
            for j in range(l, r):
                if nums[j] >= tmp:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[r] = nums[r], nums[i+1]
            return i+1

        def quicksort(nums, l, r, k):
            if l >= r:
                return
            pi = partition(nums, l, r)
            if k-1 == pi:
                return
            elif k-1 > pi:
                quicksort(nums, pi+1, r, k)
            else:
                quicksort(nums, l, pi-1, k)

        quicksort(nums, 0, len(nums)-1, k)
        return nums[k-1]
# @lc code=end
