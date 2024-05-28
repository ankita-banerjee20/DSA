class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        ptr = self.head
        count = 0
        while ptr != None:
            count += 1
            ptr = ptr.next
        return count
    
    def print(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data, end='->')
            ptr = ptr.next
    
    def insert_beg(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_any(self, data, index):
        if index < 0 or index > self.length():
            print('Index Error!')
        elif index == 0:
            self.insert_beg(data)
        else:
            ptr = self.head
            count = 0
            while count < index - 1:
                count += 1
                ptr = ptr.next
            new_node = Node(data)
            new_node.next = ptr.next
            ptr.next = new_node
            new_node.prev = ptr
            if new_node.next != None:
                ptr = new_node.next
                ptr.prev = new_node

    def insert_end(self, data):
        self.insert_any(data, self.length())

    def remove_beg(self):
        if self.head is None:
            print("List does not exist!")
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_end(self):
        ptr = self.head
        count = 0
        while count < self.length() - 2:
            count += 1
            ptr = ptr.next
        ptr.next = None

    def remove_any(self, index):
        if index < 0 or index > self.length():
            print('Index Error!')
        elif index == 0:
            self.remove_beg()
        elif index == self.length() - 1:
            self.remove_end()
        else:
            ptr = self.head
            count = 0
            while count < index - 1:
                count += 1
                ptr = ptr.next
            ptr.next = ptr.next.next
            ptr.next.prev = ptr
            
            


if __name__ == '__main__':
    a = DoublyLinkedList()
    a.insert_beg(5)
    a.insert_beg(10)
    a.insert_any(15, 1)
    a.insert_end(40)
    # a.remove_beg()
    a.remove_any(3)
    # a.remove_end()
    a.print()


