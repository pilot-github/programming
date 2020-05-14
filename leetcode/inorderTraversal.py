#######################################################################
## Given a binary tree, return the inorder traversal of its nodes' values.
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
def my_inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    if root:
        res = res + self.inorderTraversal(root.left)
        res.append(root.val)
        res = res + self.inorderTraversal(root.right)

    return res
