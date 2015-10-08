class Solution(object):
    def maxDepth(self, root):
        if (root == None):
            return 0
        x = self.maxDepth(root.left)
        y = self.maxDepth(root.right)
        if (x>=y):
            return (x+1)
        return (y+1)

#Min:60ms