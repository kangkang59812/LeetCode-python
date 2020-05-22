#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (60.64%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    41.5K
# Total Submissions: 68.5K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
# 说明：
#
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#
#
#

# @lc code=start


class Solution:
    class Heap:
        def __init__(self):
            self.heap = [(0, 0)]  # (num, num出现的次数)
            self.cnt = 0

        def push(self, x):
            x = self.heap.append(x)
            self.cnt += 1
            ind = self.cnt
            while ind > 1:
                if self.heap[ind][1] > self.heap[ind >> 1][1]:
                    temp = self.heap[ind]
                    self.heap[ind] = self.heap[ind >> 1]
                    self.heap[ind >> 1] = temp
                    ind = ind >> 1
                else:
                    break

        def pop(self):
            max_num = self.heap[1][0]
            ind = self.cnt
            self.heap[1] = self.heap[ind]
            del self.heap[-1]
            self.cnt -= 1
            ind = 1
            while ind << 1 <= self.cnt:
                swap_ind = ind
                if self.heap[ind << 1][1] > self.heap[ind][1]:
                    swap_ind = ind << 1
                if (ind << 1) + 1 <= self.cnt and self.heap[(ind << 1) + 1][1] > self.heap[swap_ind][1]:
                    swap_ind = (ind << 1) + 1
                if swap_ind == ind:
                    break
                temp = self.heap[ind]
                self.heap[ind] = self.heap[swap_ind]
                self.heap[swap_ind] = temp
                ind = swap_ind

            return max_num

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # @lc code=end
