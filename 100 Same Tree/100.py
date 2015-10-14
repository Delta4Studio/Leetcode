class Solution(object):
    def isSameTree(self, p, q):
        if (p != None) and (q != None):
            if(p.val == q.val):
                x = self.isSameTree(p.left, q.left)
                y = self.isSameTree(p.right, q.right)
            else:
                return False
        elif (p == None) and (q == None):
            return True
        else:
            return False
            
        if x and y:
            return True
        else:
            return False
#Min:40ms