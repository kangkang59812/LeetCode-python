#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (38.72%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 14.6K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#
#
# 示例：
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
# 进阶:
#
#
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
#
#
#

# @lc code=start

import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        
        self.count += 1
        heapq.heappush(self.max_heap, -num)
        max_heap_value = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_value)
        if self.count & 1:
            min_heap_value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_value)

    def findMedian(self) -> float:
        
        if self.count & 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0]+self.min_heap[0])/2
        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
        # @lc code=end
