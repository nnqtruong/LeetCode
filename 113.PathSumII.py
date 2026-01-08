# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node,remaining, path):
            if not node:
                return
            
            path.append(node.val)

            #Add current node to path
            if not node.left and not node.right and remaining == node.val:
                res.append(path[:]) # Make a copy
            
            #Explore children
            dfs(node.left,remaining - node.val,path)
            dfs(node.right,remaining - node.val,path)