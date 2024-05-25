class QueueElement():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Queue():
    def __init__(self):
        self.head = None

    def print(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data, end='->')
            ptr = ptr.next
    
    def enqueue(self, data):
        ele = QueueElement(data)
        if self.head is None:
            self.head = ele
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = ele

    def dequeue(self):
        if self.head is None:
            print('Empty queue!')
        else:
            self.head = self.head.next


if __name__ == '__main__':
    a = Queue()
    a.enqueue(5)
    a.enqueue(10)
    a.enqueue(15)
    a.enqueue(20)
    a.dequeue()
    a.dequeue()
    a.print()