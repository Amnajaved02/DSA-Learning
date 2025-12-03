''' 
    Definition of same trees: Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    Link to leetcode: https://leetcode.com/problems/same-tree/

    Problem Statement: 
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    
    Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

    Solving Approach:
    1. Use recursion to perform inorder recursion on both trees separately
    2. After getting the output compare both the arrays
    3. Return true if array is same
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """  
        if root is None:
            return [None]
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        return self.preorderTraversal(p) == self.preorderTraversal(q)