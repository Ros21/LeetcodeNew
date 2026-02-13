class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        if not itr:
            print("LinkedList is empty")
            return

        llstr=""
        while itr:
            llstr+=str(itr.data)+"-->" if itr.next else str(itr.data)
            itr=itr.next

        print(llstr)

    def insert_values(self, items):
        for item in items:
            self.insert_at_end(item)

    def insert_at_end(self,data):
        if self.head==None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)

    def length(self):
        if self.head is None:
            return 0
        itr = self.head
        length = 0
        while itr:
            itr=itr.next
            length+=1
        return length

    def insert_at(self, index, data):
        itr = self.head
        count = 0 
        while itr:
            if count==index-1:
                node = Node(data, itr.next)
                itr.next = node
            itr=itr.next
            count+=1

    def remove_at(self, index):
        if index<0 or index>=self.length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return 

        itr = self.head
        count = 0
        while itr:
            if count==index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1




ll = LinkedList()
# ll.insert_at_beginning(5)
# ll.insert_at_beginning(6)
# ll.print()
# ll.insert_at_end(44)
# ll.insert_at_end(33)
# ll.print()
ll.insert_values(["banana","mango","grapes","orange"])
# ll.length()
ll.insert_at(1,"blueberry")
ll.print()
ll.remove_at(1)
ll.print()

# ll.insert_values([45,7,12,567,99])
# ll.insert_at_end(67)
# ll.print()
# ll.length()