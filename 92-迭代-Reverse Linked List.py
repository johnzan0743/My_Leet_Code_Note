# 92-迭代-Reverse Linked List.py
class Solution:
    def reverseBetween(self,head,m,n):
        dummy = ListNode(0)
        dummy.next = head
        pre_m =  dummy
        
        for i in range(m-1):
            pre_m = pre_m.next  # pre_m (0) --> 1
        
        previous = None
        current = pre_m.next
        for i in range(n-m+1): # previous = 4 current = 5
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        pre_m.next.next = current # pre_m = 1, pre_m.next = 2, current = 5
        pre_m.next = previous
        return dummy.next