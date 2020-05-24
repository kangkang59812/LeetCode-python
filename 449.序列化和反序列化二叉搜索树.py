#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (50.88%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 10.1K
# Testcase Example:  '[2,1,3]'
#
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
#
# 设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。
# 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
#
# 编码的字符串应尽可能紧凑。
#
# 注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # def dfs(root, s):
        #     if not root:
        #         s += 'null,'
        #     else:
        #         s += str(root.val)+','
        #         s = dfs(root.left, s)
        #         s = dfs(root.right, s)
        #     return s
        # return dfs(root, '')
        if not root:
            return "null,"
        stack = [root]
        ss = [str(root.val)+","]
        s = ""
        while stack:
            p = stack.pop()
            s += ss.pop()
            if p:
                if p.right:
                    stack.append(p.right)
                    ss.append(str(p.right.val)+",")
                else:
                    stack.append(None)
                    ss.append("null,")
                if p.left:
                    stack.append(p.left)
                    ss.append(str(p.left.val)+",")
                else:
                    stack.append(None)
                    ss.append("null,")
        return s

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def dfs(lists):
            if lists[0] == 'null':
                lists.pop(0)
                return None
            root = TreeNode(int(lists[0]))
            lists.pop(0)
            root.left = dfs(lists)
            root.right = dfs(lists)
            return root

        lists = data.split(',')[:-1]
        return dfs(lists)
      
        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
        # @lc code=end
