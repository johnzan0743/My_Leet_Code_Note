# 单向链表的实现
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Singe_linked_list:
    def __init__(self,node=None):
        self.__head = node
    
    def head_add(self,val): # 从头部位置插入
        node = Node(val)
        node.next = self.__head
        self.__head = node
    def tail_add(self,val):
        node = Node(val)
        current = self.__head
        if not current:
            self.head_add(val)
        else:
            while current.next:
                current = current.next
            current.next = node

    def traverse(self):
        current = self.__head
        while current:
            print(current.val)
            current = current.next
A = Singe_linked_list()
A.head_add(1)
A.head_add(2)
A.head_add(3)
A.tail_add(4)
A.tail_add(5)
A.tail_add(6)
A.traverse()
