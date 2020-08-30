#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Easy (29.60%)
# Likes:    103
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 28.6K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
#
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
#
# 说明:
#
#
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。
#
#
# 示例 1:
#
#
# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
#
#
# 示例 2:
#
#
# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
#
#
#

# @lc code=start


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        #    1、找到每个房屋离加热器的最短距离（即找出离房屋最近的加热器）
        #    2、在所有距离中选出最大的一个max(res)即为结果
        res = []
        heaters.sort()
        for house in houses:
            left = 0
            right = len(heaters)-1
            while left < right:
                middle = left+(right-left)//2
                # if heaters[middle] > house:
                #     right = middle-1
                if heaters[middle] < house:
                    left = middle+1
                else:
                    right = middle

            if heaters[left] == house:
                res.append(0)
            elif heaters[left] < house:
                res.append(house-heaters[left])
            elif left == 0:
                res.append(heaters[left]-house)
            else:
                res.append(min(heaters[left]-house, house-heaters[left-1]))
        return max(res)
        # @lc code=end
