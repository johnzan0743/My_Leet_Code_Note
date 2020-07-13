# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = current = ListNode(0)
        dummy.next = head
        current.next = head
        while current.next and current.next.next:
            first = current.next 
            second = current.next.next
            # current = 0  first = 1  second = 2
            # 0 -> 1 -> 2 -> 3

            current.next = second
            # 0 -> 2

            first.next = second.next
            # 1 -> 3

            second.next = first
            # 2 -> 1

            current = current.next.next
            # 0 -> 2 -> 1(current) -> 3
        return dummy.next

# 此题的套路：
# first = current.next
# second = current.next.next
# current.next = second 
# 初始化新一轮循环的current位置
# 注意：因为已经初始化了新循环的current位置，所以新循环的first/second不用再操心了

# first.next = second.next 
# second.next = first

'''
这种linked list题目，我目前个人理解的套路是：
1. 如果没有head或者head.next，则返回head
2. 定义一个dummy node=ListNode（0）
3. dummy.next = head
4. dummy = current
5. 限定条件（循环）
6. 如果需要定义新的node，则优先定义 x_node = current.next
7. 然后先定义node.next指针
8. 把所有node.next指针位置定义好之后，就可以移动current_node位置了
'''


        
