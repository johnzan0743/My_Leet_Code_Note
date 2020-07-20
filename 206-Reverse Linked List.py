class Solution(object):
    def reverseList(self, head):
        previous = None 
        # 因为任何单向链表都是以Null/None为结束，所以这里一定要定义previous = None
        current = head
        # （0） -> 1 -> 2
        #  pre   curr temp
        while current:
            temp = current.next
            # (0) -> 1 -> 2
            current.next = previous
            # 1 -> (0).....2 -> 3
            previous = current
            current = temp
            # pre : 1 
            # current: 2
            # temp = 3
        return previous
# 在linked list中，当 X.next处于等号左边时，表示（重新）定义X node的next指针方向
# 当 Y.next处于等号右边时，表示把Y node的next指针方向赋予给某node 或某node的next指针
# 或移动Y node：Y = Y.next