LinkedList总结：

1. 每一个linked list上的node都有两个属性，一个是val，另一个是next
2. 在不手动更改val的前提下，val的变化即意味着list node位置的变化，即当前的list node已经移动到另外一个node里了，这有点像一个萝卜一个坑。每一个node就是一个萝卜坑。而next则只是一个指针的方向，即预备的下一目的地，next类似于指南针，或者预瞄准

3. A = A.next 说明A的index移动到了A.next所指的指针位置，即A真的有移动位置
4. A.next = B.next 说明A的下一个指针位置被定义到目前B的下一个指针所指的位置上，此时B的下一指针位置不变，但是A的下一指针位置变了
5. B=A.next 说明B的位置移动到了A的下一个指针位置，即B真的移动了位置

经典三指针互换list node position
![](2020-07-05-16-29-18.png)
   
求linked list 长度（length）
def len_link(list):
    temp=list.head
    count=0
    while(temp):
        count+=1
        temp=temp.next
    return count