#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (44.47%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 75.5K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
#
# 提示：
#
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
#
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？
#
#

# @lc code=start


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        n = len(nums)
        if n == 0 or k < 1:
            return []
        if k == 1:
            return nums
        if n <= k:
            return [max(nums)]

        window = deque()
        res = []

        for i in range(k):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
        for i in range(k, n):
            res.append(nums[window[0]])
            if i-window[0] >= k:
                window.popleft()
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
        res.append(nums[window[0]])
        return res
        # @lc code=end
