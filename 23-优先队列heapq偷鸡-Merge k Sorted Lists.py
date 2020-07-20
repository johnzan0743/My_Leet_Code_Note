class Solution:
    def mergeKLists(self,lists):
        if not lists or len(lists) == 0:
            return 0
        import heapq
        heap = []
        for nodes in lists:
            while nodes:
                heapq.heappush(heap,nodes.val)
                nodes = nodes.next
        dummy = ListNode(0)
        current = dummy
        while heap:
            current.next = ListNode(heapq.heappop(heap))
            current = current.next
        return dummy.next

