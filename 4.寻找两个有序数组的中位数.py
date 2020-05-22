#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (35.94%)
# Likes:    1518
# Dislikes: 0
# Total Accepted:    90.6K
# Total Submissions: 252K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#
### 垃圾
# nums3 = []
# i, j = 0, 0
# while (i < len(nums1)) and (j < len(nums2)):

#     if nums1[i] > nums2[j]:
#         nums3.append(nums2[j])
#         j += 1
#     else:
#         nums3.append(nums1[i])
#         i += 1

# if i < len(nums1):
#     nums3.extend(nums1[i:])
# if j < len(nums2):
#     nums3.extend(nums2[j:])
# if len(nums3) % 2 == 0:
#     return (nums3[len(nums3)//2]+nums3[len(nums3)//2-1])/2
# else:
#     return nums3[len(nums3)//2]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1),len(nums2)
        if m>n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n==0:
            raise ValueError
        imin,imax,half_len=0,m,(m+n+1)//2

        
    

