# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Object:
    
    def __init__(self, root:TreeNode, runningSum : int, path:List[int]):
        self.root = root
        self.runningSum = runningSum
        self.path  = path
    
    def getNode(self):
        return self.root
    
    def getRunningSum(self):
        return self.runningSum
    
    def getPath(self):
        return self.path
        

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        runningSum = 0
        stack = []
        path = []
        result = []
        while root is not None or stack:
            while root is not None:
                runningSum += root.val
                path.append(root.val)  #this is causing the problem.
                stack.append(Object(root,runningSum,list(path)))
                root = root.left
            
            o = stack.pop()
            root = o.getNode()
            path = o.getPath()
            runningSum = o.getRunningSum()
            

            if root.left is None and root.right is None:
                if runningSum == targetSum:
                    result.append(path)
                    
            root = root.right
        
        return result
    
    
#      iterative solution -- doing what recurssion does under the hood.
