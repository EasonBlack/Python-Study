#   Given linked list: 1->2->3->4->5, and n = 2.

#   After removing the second node from the end, the linked list becomes 1->2->3->5.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        length  = 0
        first = head
        while first != None:
            length+=1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length-=1
            first = first.next
        first.next = first.next.next
        return dummy.next
    
        


L1 = ListNode(9)
L2 = ListNode(4)
L3 = ListNode(3)
L4 = ListNode(1)
L1.next = L2
L2.next = L3
L3.next = L4

a =  Solution().removeNthFromEnd(L1, 1)
while True:
    print a.val
    if a.next == None :
        break
    a = a.next