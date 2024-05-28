class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_children(self, trees):
        self.children.append(trees)
        trees.parent = self 

    def get_level(self):
        level = 0
        while self.parent != None:
            self = self.parent
            level += 1
        return level

    def print_tree(self):
        branch = self.get_level() * ' ' + '|__' if self.get_level() else ''
        print(branch + self.data)
        for tree in self.children:
            tree.print_tree()




if __name__ == '__main__':
    root = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')

    root.add_children(b)
    root.add_children(c)
    root.add_children(d)

    b.add_children(e)
    b.add_children(f)

    c.add_children(g)


    root.print_tree()
