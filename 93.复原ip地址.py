#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (46.23%)
# Likes:    283
# Dislikes: 0
# Total Accepted:    47.1K
# Total Submissions: 100.2K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
#
#
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
#
#

# @lc code=start


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(path, begin, s):
            if len(path) == 4 and begin == len(s):
                tmp = "".join(x+'.' for x in path)
                res.append(tmp[:-1])
            i = begin
            if i < len(s):
                path.append(s[i])
                backtrack(path, i+1, s)
                path.pop()
                # 防止 0*开头
                if i+1 < len(s) and int(s[i:i+2]) <= 255 and s[i] != '0':
                    path.append(s[i:i+2])
                    backtrack(path, i+2, s)
                    path.pop()
                # 防止0**开头
                if i+2 < len(s) and int(s[i:i+3]) <= 255 and s[i] != '0':
                    path.append(s[i:i+3])
                    backtrack(path, i+3, s)
                    path.pop()
        # 小于最短，大于最长排除
        if len(s) > 12 or len(s) < 4:
            return []
        res = []
        path = []
        backtrack(path, 0, s)
        return res
# @lc code=end
