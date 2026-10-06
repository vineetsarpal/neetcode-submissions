# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Edge cases
        if not subRoot:
            return True 
            # since null is a subroot of root. For e.g. leaf nodes will have null
            # as child nodes. Also null root and null subroot is a true case
        
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    def sameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.sameTree(p.left, q.left) and
                    self.sameTree(p.right, q.right))
        return False
        