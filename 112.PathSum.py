# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        #Check if root
        if not root:
             return False

        #Check if we're at a leaf
        if not root.left and not root.right:
            return root.val == targetSum

        #Recruse on children with reduced target
        new_target = targetSum - root.val
        return (self.hasPathSum(root.left,new_target) or self.hasPathSum(root.right,new_target))
