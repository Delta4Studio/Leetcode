class Solution(object):
    def minDepth(self, root):
        if (root == None):
            return 0
        x = self.minDepth(root.left)
        y = self.minDepth(root.right)
        if x==0 or y==0:
            if x==0:
                return y+1
            return x+1
        if (x<=y):
            return (x+1)
        return (y+1)

#Min:64ms