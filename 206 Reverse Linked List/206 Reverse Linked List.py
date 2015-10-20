class Solution(object):
    def reverseList(self, head):
        cp = head
        np = None
        while cp != None :
            pp = cp.next
            cp.next = np
            np = cp
            cp = pp
        return np
#Min:56ms