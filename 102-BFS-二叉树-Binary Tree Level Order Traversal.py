# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root] #初始化队列
        result = []
        while queue:
            current = []
            nxt = [] # 保存下一层的节点
            for node in queue:
                current.append(node.val)  # # 保存当前层的遍历值，因为queue保存的是TreeNode类型
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            result.append(current)
            queue = nxt #更新队列
        return result
# current保存的是当前节点的值
# 而nxt保存的是下一层的二叉树节点（TreeNode)
