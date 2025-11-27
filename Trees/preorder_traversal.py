''' 
    Definition of Preorder traversal: https://www.geeksforgeeks.org/dsa/preorder-traversal-of-binary-tree/ 
    Link to leetcode: https://leetcode.com/problems/binary-tree-preorder-traversal/

    Problem Statement: 
    Given the root of a binary tree, return the preorder traversal of its nodes' values.

    Example 1:
    Input: root = [1,null,2,3]
    Output: [1,2,3]

    Example 2:
    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    Output: [1,2,4,5,6,7,3,8,9]


    Solving Approach:
    1. Use recursion -- might not work for in depth trees
    2. Append the value of the current node to the results array
    3. Iterate on left subtree and then right
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.preorder_traversal_output = []

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return self.preorder_traversal_output

        self.preorder_traversal_output.append(root.val)

        if root.left:
            self.preorderTraversal(root.left)

        if root.right:
            self.preorderTraversal(root.right) 

        return self.preorder_traversal_output    

        
        