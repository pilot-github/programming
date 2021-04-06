#######################################################################
## Given a binary tree, return the postorder traversal of its nodes' values.
## Example:
## Input: [1,null,2,3]
##    1
##     \
##      2
##     /
##    3
## 
## Output: [1,3,2]
#######################################################################


def postorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    
    if root:
        res = res + self.postorderTraversal(root.left)
        res = res + self.postorderTraversal(root.right)
        res.append(root.val)
    
    return res