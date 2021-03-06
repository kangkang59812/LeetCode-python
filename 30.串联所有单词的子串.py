#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (30.06%)
# Likes:    265
# Dislikes: 0
# Total Accepted:    33.3K
# Total Submissions: 108.7K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
#
#
# 示例 1：
#
# 输入：
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#
#
# 示例 2：
#
# 输入：
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# 输出：[]
#
#
#

# @lc code=start


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        word_num = len(words)
        word_len = len(words[0])
        all_len = word_len*word_num
        if all_len > len(s):
            return []
        word_counter = Counter(words)
        res = []
        for i in range(len(s)-all_len+1):
            tmp = [s[j:word_len+j] for j in range(i, i+all_len, word_len)]
            s_counter = Counter(tmp)
            if s_counter == word_counter:
                res.append(i)
        return res
# @lc code=end
