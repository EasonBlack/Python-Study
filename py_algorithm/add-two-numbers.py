
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#321
L1 = ListNode(9)
L2 = ListNode(9)
L1.next = L2


#231
M1 = ListNode(1)


class Solution(object):
    def addTwoNumbers(self, l1, m1):
        store = []
        current, result, extra  = None, None, 0
        l, m = l1, m1
        while True:
            store.append(l.val + m.val)
            if l.next == None and m.next == None:
                break 
            else:
                l,m = l.next or ListNode(0),m.next or ListNode(0)
        print store
        for single in store:
            displayNum = (single % 10 + extra) % 10
            real = single + extra
            extra = real // 10
            node = ListNode(displayNum)
            
            if result:
                current.next = node
                current = current.next
            else:
                current = node
                result = current
        print extra , 'xxxxx'
        if extra != 0:
            node = ListNode(0 + extra)
            current.next = node

        return result

a = Solution()
r = a.addTwoNumbers(L1, M1)
while True:
    print r.val
    if r.next == None:
        break 
    else:
        r = r.next

# print a.addTwoNumbers(L1, M1)
