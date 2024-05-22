class Node:
    def __init__(self, data= None, next=None):
        self.data = data
        self.next = next

class LinkedList:
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
        if self.head is None:
            self.head = Node(data)
        else:
            start_node = Node(data)
            start_node.next = self.head
            self.head = start_node

    def insert_any(self, data, index):
        if index < 0 or index > self.length():
            print("Index Error!")
        elif index == 0:
            self.insert_beg(data)
        else:
            ptr = self.head
            i = 0
            while i < index - 1:
                i += 1
                ptr = ptr.next
            new_node = Node(data)
            new_node.next = ptr.next
            ptr.next = new_node

    def insert_end(self, data):
        self.insert_any(data, self.length())

    def insert_by_val(self, data, value):
        new_node = Node(data)
        ptr = self.head
        while ptr.data != value:
            ptr = ptr.next
        new_node.next = ptr.next
        ptr.next = new_node

    def delete_beg(self):
        if self.head == None:
            print('Empty Linked List')
        else:
            self.head = self.head.next

    def delete_any(self, index):
        if index < 0 or index >= self.length():
            print("Index Error!")
        elif index == 0:
            self.delete_beg()
        else:
            ptr = self.head
            i = 0
            while i < index-1:
                ptr = ptr.next
                i += 1

            ptr.next = ptr.next.next

    def delete_end(self):
        self.delete_any(self.length() - 1)

    def delete_by_value(self, value):
        ptr = self.head
        while ptr.next.data != value:
            ptr = ptr.next
        ptr.next = ptr.next.next

if __name__ == '__main__':
    a = LinkedList()
    a.insert_beg(5)
    a.insert_beg(10)
    a.insert_any(15, 0)
    a.insert_end(40)
    # a.delete_any(3)
    # a.delete_beg()
    a.print()
    print()
    a.insert_by_val(50, 5)
    a.print()
    print()
    a.delete_by_value(40)
    a.print()
    