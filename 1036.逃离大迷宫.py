#
# @lc app=leetcode.cn id=1036 lang=python3
#
# [1036] 逃离大迷宫
#
# https://leetcode-cn.com/problems/escape-a-large-maze/description/
#
# algorithms
# Hard (26.39%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 4.3K
# Testcase Example:  '[[0,1],[1,0]]\n[0,0]\n[0,2]'
#
# 在一个 10^6 x 10^6 的网格中，每个网格块的坐标为 (x, y)，其中 0 <= x, y < 10^6。
#
# 我们从源方格 source 开始出发，意图赶往目标方格 target。每次移动，我们都可以走到网格中在四个方向上相邻的方格，只要该方格不在给出的封锁列表
# blocked 上。
#
# 只有在可以通过一系列的移动到达目标方格时才返回 true。否则，返回 false。
#
#
#
# 示例 1：
#
# 输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# 输出：false
# 解释：
# 从源方格无法到达目标方格，因为我们无法在网格中移动。
#
#
# 示例 2：
#
# 输入：blocked = [], source = [0,0], target = [999999,999999]
# 输出：true
# 解释：
# 因为没有方格被封锁，所以一定可以到达目标方格。
#
#
#
#
# 提示：
#
#
# 0 <= blocked.length <= 200
# blocked[i].length == 2
# 0 <= blocked[i][j] < 10^6
# source.length == target.length == 2
# 0 <= source[i][j], target[i][j] < 10^6
# source != target
#
#
#

# @lc code=start


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        stack = [source]
        m, n = abs(source[0]-target[0])+1, abs(source[1]-target[1])+1
        matrix = [[0]*n for _ in range(m)]
        for block in blocked:
            if source[0] <= block[0] <= target[0] and source[1] <= block[1] <= target[1]:
                matrix[block[0]][block[1]] = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while stack:
            cur_pos = stack.pop()
            if cur_pos[0] == target[0] and cur_pos[1] == target[1]:
                return True
            for d in directions:
                if source[0] <= cur_pos[0]+d[0] <= target[0] and source[1] <= cur_pos[1]+d[1] <= target[1] and matrix[cur_pos[0]+d[0]][cur_pos[1]+d[1]] != -1 and matrix[cur_pos[0]+d[0]][cur_pos[1]+d[1]] != 1:
                    stack.append([cur_pos[0]+d[0], cur_pos[1]+d[1]])
                    matrix[cur_pos[0]+d[0]][cur_pos[1]+d[1]] = -1
        return False


# @lc code=end
