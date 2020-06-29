class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        true_pointer = dummy
        i = 0
        
        while pointer.next:
            pointer = pointer.next
            i +=1
        for j in range(i-n):
            true_pointer = true_pointer.next

        true_pointer.next = true_pointer.next.next
        
        return dummy.next
            