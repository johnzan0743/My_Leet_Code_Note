# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 and l2:
            current.next = ListNode((l1.val+l2.val+carry) % 10)
            #ListNode相当于给current.next赋值
            #ListNode(X)相当于instantiate一个新的Node，里面包含val和next
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            current = current.next
        while l1:
            current.next = ListNode((l1.val+carry) % 10)
            carry = (l1.val + carry) //10
            l1 = l1.next
            current = current.next
        while l2:
            current.next = ListNode((l2.val+carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            current = current.next
        if carry == 1:
            current.next = ListNode(1)
        
        return dummy.next