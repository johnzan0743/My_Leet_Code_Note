class Solution(object):
    def reverseList(self, head):
        previous = None
        current = head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous