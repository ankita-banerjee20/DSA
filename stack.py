class StackElement():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack():
    def __init__(self):
        self.head = None

    def print(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data, end='->')
            ptr = ptr.next

    def push(self, data):
        ele = StackElement(data)
        if self.head is None:
            self.head = ele
        else:
            ele.next = self.head
            self.head = ele

    def pop(self):
        if self.head is None:
            print('Stack is empty')
        else:
            self.head = self.head.next

    def peek(self):
        print('Last element: ', self.head.data)

if __name__ == '__main__':
    a = Stack()
    a.push(5)
    a.push(10)
    a.pop()
    a.print()
    print()
    a.peek()