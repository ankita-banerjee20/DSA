class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_children(self, data):
        if self.data == data:
            print("Node already exists!")
        elif data < self.data:
            if self.left:
                self.left.add_children(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_children(data)
            else:
                self.right = BinaryTreeNode(data)
    
    def in_order_traversal(self):
        nodes = []

        if self.left:
            nodes += self.left.in_order_traversal()

        nodes.append(self.data)

        if self.right:
            nodes += self.right.in_order_traversal()

        return nodes
    
    def min_node(self):
        if self.left is None:
            return self.data

        return self.left.min_node()
    


    def delete_node(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_value = self.right.min_node()
            self.data = min_value
            self.right = self.right.delete_node(min_value)

        return self
            
        

if __name__ == '__main__':
    bst = BinaryTreeNode(20)
    bst.add_children(10)
    bst.add_children(15)
    bst.add_children(17)
    bst.add_children(8)
    bst.add_children(25)
    bst.add_children(23)
    bst.add_children(27)
    bst.delete_node(23)

    print(bst.in_order_traversal())
