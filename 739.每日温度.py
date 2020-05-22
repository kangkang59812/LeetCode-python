#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (59.08%)
# Likes:    252
# Dislikes: 0
# Total Accepted:    34.2K
# Total Submissions: 57.8K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
#
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4,
# 2, 1, 1, 0, 0]。
#
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
#
#

# @lc code=start


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        wait = []
        wait.append((0, T[0]))
        r = [0]*len(T)
        for i, t in enumerate(T[1:]):
            index = i+1

            # 栈空
            if len(wait) == 0:
                wait.append((index, t))
                continue

            # 和顶部数据对比,同时还要把自己入栈
            # 先判断是否为空，不然为空的话不能索引；短路与
            while len(wait) != 0 and t > wait[-1][1]:
                r[wait[-1][0]] = index-wait[-1][0]
                wait.pop()

            wait.append((index, t))
        return r
        # @lc code=end
