# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
递归
每次输出一个元组,(含此节点的最大值、不含此节点的最大值)
result =max((root.val+f(ll)+f(lr)+f(rl)+f(rr)),f(l)+f(r))
f(n) = max(rob,no_rob)
"""


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # [偷当前屋子的]
        memo = {None: (0, 0)}
        stack = [(False, root)]

        while len(stack) != 0:
            symbol, node = stack.pop()

            if node is None:
                continue

            # 首先会一直向栈中压入数据,一直到将所有的所有的节点都被压入之后才结束
            if not symbol:
                stack.extend(([1, node], [0, node.right], [0, node.left]))
            else:
                # 不选当前节点的最大值,选当前节点的最大值
                memo[node] = max(memo[node.left]) + max(memo[node.right]), \
                             node.val + memo[node.left][0] + memo[node.right][0]
        return max(memo[root])
