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
        memo = {}
        result = self.helper(root,memo)
        return max(result)

    def helper(self, node, memo):
        if node is None:
            return 0, 0
        if node in memo:
            return memo[node]
        # 不选当前
        left = self.helper(node.left, memo)
        right = self.helper(node.right, memo)
        # (不选当前的=左右的最大值之和,选择当前的=当前的值+选左节点+选右节点)
        memo[node] = (max(left) + max(right), node.val + left[0] + right[0])
        return memo[node]
