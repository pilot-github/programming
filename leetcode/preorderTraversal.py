#######################################################################
## Given a binary tree, return the pre order traversal of its nodes' values.
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
 
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    if root:
        res.append(root.val)
        res = res + self.preorderTraversal(root.left)
        res = res + self.preorderTraversal(root.right)
        
    return res