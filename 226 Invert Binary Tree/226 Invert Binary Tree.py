class Solution(object):
    def invertTree(self, root):
        if root != None:
            x = root.left;
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(x)
            return root
        else:
            return None
#Min:36ms
        