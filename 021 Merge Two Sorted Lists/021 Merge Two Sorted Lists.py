class Solution(object):
    def mergeTwoLists(self, l1, l2):
        x = ListNode(0)
        p = x
        while (l1 != None) or (l2 != None):
            if l2 == None :
                p.next = l1
                break
            elif l1 == None :
                p.next = l2
                break
            elif (l1.val > l2.val) :
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        return x.next
#Min:52ms