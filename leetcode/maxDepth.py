##########################################################################################
## Given binary tree [3,9,20,null,null,15,7],
## return its depth = 3.
##          3
##         / \
##        9  20
##          /  \
##         15   7
##
## link = "https://leetcode.com/problems/maximum-depth-of-binary-tree/"
##########################################################################################

def my_maxDepth(self, root: TreeNode) -> int:
    depth = 0
    left_depth = 0
    right_depth = 0
    if root and root.val is not None:
        depth = depth + 1
        if root.left:
            left_depth = self.maxDepth(root.left)
        if root.right:
            right_depth = self.maxDepth(root.right)

        if left_depth > right_depth:
            depth += left_depth
        else:
            depth += right_depth
    return depth
    
def maxDepth(self, root):
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0



