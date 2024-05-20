class Node:
    def __init__(self, data= None, next=None):
        self.data = data
        self.next = next

class Linked_list:
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
        if index < 0 or index >= self.length():
            print("Index Error!")
        elif index == 0:
            self.insert_beg(data)
        else:
            ptr = self.head
            i = 0
            while i < index:
                i += 1
                ptr = ptr.next
            new_node = Node(data)
            new_node.next = ptr.next
            ptr.next = new_node

    def insert_end(self, data):
        self.insert_any(data, self.length() - 1)




    


if __name__ == '__main__':
    a = Linked_list()
    a.insert_beg(5)
    a.insert_beg(10)
    a.insert_any(15, 0)
    a.insert_end(40)
    a.print()
    