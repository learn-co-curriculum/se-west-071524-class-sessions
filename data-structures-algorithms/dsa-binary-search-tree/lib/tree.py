# class Tree:
#   def __init__(self, root = None):
#     self.root = root

#   def get_element_by_id(self, id):
#     pass


class Node:

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


class BSTree:

    def __init__(self):
        self.root = None
        self.size = 0

    # def insert(self, value): # procedural
    #     node = Node(value)
    #     if not self.root:
    #         self.root = node
    #         return
    #     current = self.root
    #     while current:
    #         if node.value < current.value:
    #             if not current.left:
    #                 current.left = node
    #                 return
    #             current = current.left
    #         elif node.value >= current.value:
    #             if not current.right:
    #                 current.right = node
    #                 return
    #             current = current.right

    def insert(self, value):
        self.size += 1
        if not self.root:
            self.root = Node(value)
        else:
            self.insertWithNode(self.root, value)

    def insertWithNode(self, node, value):  # recursively add to BST
        if not node.left and not node.right:
            newNode = Node(value)
            if value >= node.value:
                node.right = newNode
            else:
                node.left = newNode
        else:
            if value >= node.value:
                if node.right:
                    self.insertWithNode(node.right, value)
                else:
                    newNode = Node(value)
                    node.right = newNode
            else:
                if node.left:
                    self.insertWithNode(node.left, value)
                else:
                    newNode = Node(value)
                    node.left = newNode

    def print(self):
        new_line = Node("|")
        queue = [self.root, new_line]
        result = ""
        while len(queue):
            curr = queue.pop(0)
            result += f"{str(curr.value)} "
            if curr == new_line and len(queue):
                queue.append(new_line)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print(result)


t = BSTree()
t.insert(13)
t.insert(9)
t.insert(17)
t.insert(2)
t.print()
