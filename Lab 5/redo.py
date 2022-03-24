class TreeNode:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, key):
        """Takes key as an input and inserts the new node with the key into the correct spot"""
        if self.key is None:
            self.key = key
        else:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                    self.left.parent = self
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                    self.right.parent = self
                else:
                    self.right.insert(key)

    def find_successor(self):
        """returns the successor when of the removed node"""
        if self.right is None:
            return self
        current = self.right
        while current.left is not None:
            current = current.left
        return current

    def find_min(self):
        """returns min value in the tree"""
        current = self
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self):
        """returns max value in the tree"""
        current = self
        while current.right is not None:
            current = current.right
        return current.key

    def inorder_print_tree(self):
        """prints the in order of the subtree of self"""
        if self.left is not None:
            self.left.inorder_print_tree()
        print(self.key)
        if self.right is not None:
            self.right.inorder_print_tree()

    def print_levels(self):
        """print the inorder traversal lists of pairs, [key, level of the node] with root being level 0"""
        start = self
        while start.parent is not None:
            start = start.parent

        if self.left is not None and self.left.key is not start.key:
            self.left.print_levels()
        count = 0

        while self.key is not start.key:
            if self.key < start.key:
                count += 1
                start = start.left
            else:
                count += 1
                start = start.right
        print([self.key, count])
        if self.right is not None and self.right.key is not start.key:
            self.right.print_levels()


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        """returns true if the key is in a node in the tree"""
        current = self.root
        while current is not None and current.key is not key:
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False
        else:
            return True


    def insert(self, newKey):
        """inserts the new node containing the newKey into the tree in the correct spot"""
        if self.root is None:
            self.root = TreeNode(newKey)
            return
        else:
            current = self.root
            if current.key > newKey:
                if current.left is None:
                    current.left = TreeNode(newKey)
                    current.left.parent = current
                else:
                    current.left.insert(newKey)

            else:
                if current.right is None:
                    current.right = TreeNode(newKey)
                    current.right.parent = current
                else:
                    current.right.insert(newKey)

    def delete(self, key):
        current = self.root
        while current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        self.delete_node(current)

    def delete_node(self, current):

        """No child case"""
        if current.left is None and current.right is None:
            if current.key == self.root.key:
                self.root = None

            else:
                current.key = None

        """One child case"""
        if current.left is None or current.right is None:
            if current.left is not None:
                current.key = current.left.key
                current.left = None
            if current.right is not None:
                current.key = current.right.key
                current.right = None

            """Two child case"""
        else:

            temp = current.find_successor()
            print(temp.key)

            self.delete_node(current.find_successor())

            temp_left = current.left
            temp_right = current.right
            temp.parent = current.parent
            print(temp_left.key)
            print(temp_right.key)
            print(temp.key)

            if current.parent.right == current:
                current.parent.right = temp
            else:
                current.parent.left = temp

            current = temp
            current.left = temp_left
            current.right = temp_right


    def print_tree(self):
        """print inorder the entire tree"""
        root = self.root
        if root.left is not None:
            root.left.inorder_print_tree()
        print(root.key)
        if root.right is not None:
            root.right.inorder_print_tree()


tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(6)
#tree.insert(15)
#tree.insert(17)
#tree.insert(19)
tree.print_tree()

#tree.delete(17)
print("")
tree.delete(5)
#tree.print_tree()


print("")
print(tree.root.key)
print(tree.root.left.key)
#print(tree.root.left.left.key)
#print(tree.root.left.right.key)
#print(tree.root.left.left.left.key)
#print(tree.root.right.key)
#print(tree.root.right.key)
#print(tree.root.right.right.key)

