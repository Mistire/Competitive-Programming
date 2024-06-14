class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    #If there is a print 
    def __str__(self):
        #[1,2,3,4]
        arr = [self.head]
        temp = self.next
        while temp:
            arr.append(temp.value)
            temp = temp.next
        return '->'.join(map(str, arr))


class MyLinkedList(object):

    def __init__(self):
       self.head = Node()

    def get(self, index):
        temp = self.head

        for _ in range(index + 1):
            temp = temp.next
    
            if not temp:
                return -1
        return temp.val

    def addAtHead(self, val):
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def addAtTail(self, val):
        newNode = Node(val)
        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = newNode
        
    def addAtIndex(self, index, val):
        newNode = Node(val)
        temp = self.head
        for _ in range(index):
            temp = temp.next
            if temp == None:
                return
        newNode.next = temp.next
        temp.next = newNode

    def deleteAtIndex(self, index):
        temp = self.head

        for _ in range(index):
            temp = temp.next
            if not temp.next:
                return

        temp.next = temp.next.next

        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)