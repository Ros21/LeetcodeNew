class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        itr = self.head
        count = 0
        while itr:
            if count == index:
                return itr.data
            itr = itr.next
            count+=1
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        self.head = Node(val,self.head)
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, None)
            self.size+=1
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(val, None)
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return -1

        if index <= 0:
            self.addAtHead(val)
            return

        if index==self.size:
            self.addAtTail(val)
            return
        

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(val, itr.next)
            itr = itr.next
            count+=1
        self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:


        if index>=self.size or index<0:
            return -1

        itr = self.head
        if index == 0:
            self.head = itr.next

        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            itr = itr.next
            count+=1
        self.size-=1


    def print(self):
        itr = self.head
        nodestr=""
        while itr:
            nodestr+=str(itr.data)+ "-->" if itr.next else str(itr.data)
            itr = itr.next
        print(nodestr)
        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(4)
obj.addAtHead(2)
# obj.addAtTail(5)
# obj.addAtTail(6)
# obj.print()
# param_1 = obj.get(-1)
# print(param_1)
obj.addAtIndex(0,10)     # 2--4--
obj.addAtIndex(0,20)
obj.addAtIndex(1,30)
obj.print()
obj.deleteAtIndex(0)
obj.deleteAtIndex(0)
obj.deleteAtIndex(0)
obj.print()
