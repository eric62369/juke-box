
class BinarySearchTreeSet():
    '''
        A simple implementation of a binary search tree. Will not enforce correct typing during
        comparisons. Not self-balancing yet.
    '''
    class Node():
        '''
            A node in the BinarySearchTreeSet. Is meant to function like a private inner class in
            Java.
        '''
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

        def __str__(self):
            return "Node: " + str((self.data, self.left.__str__(), self.right.__str__()))

    def __init__(self):
        self.overallRoot = None

    def add(self, data):
        def add(data, root=None):
            if root is None:
                root = BinarySearchTreeSet.Node(data=data)
            else:
                if root.data > data:  # data goes left
                    root.left = add(data=data, root=root.left)
                elif root.data < data:  # data goes right
                    root.right = add(data=data, root=root.right)
                else:
                    root = BinarySearchTreeSet.Node(data, root.left, root.right)
            return root
        self.overallRoot = add(data=data, root=self.overallRoot)

    def __str__(self):
        result = "BinarySearchTreeSet:"
        def inorder(root=None):
            stringData = ""
            if root is not None:
                stringData += inorder(root.left)
                stringData += " " + str(root.data)
                stringData += inorder(root.right)
            return stringData
        result += inorder(self.overallRoot)
        return result

if __name__ == "__main__":
    tree = BinarySearchTreeSet()
    tree.add(1)
    tree.add(3)
    tree.add(2)
    tree.add(2)
    tree.add(5)
    print(tree)
