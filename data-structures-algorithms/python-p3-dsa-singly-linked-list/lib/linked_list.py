class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append(self, node):
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        return

    def print(self):
        if not self.head:
            print("Empty list")
            return
        curr = self.head
        result = ""
        while curr.next:
            result += str(curr)
            curr = curr.next
        result += str(curr)
        print(result)

    def find(self, target):
        if not self.head:
            print("Empty list")
            return
        curr = self.head
        while curr.next:
            if curr.value == target:
                return curr
            curr = curr.next
        return "Not found"

    # def insert_after(self, target_node, new_node):
    #     if not target_node or not new_node:
    #         print("args must be nodes")
    #     new_node.next = target_node.next
    #     target_node.next = new_node

    # def insert_at_index(self, index, node):
    #     curr = self.head
    #     for _ in range(index):
    #         if not curr.next:
    #             print("index out of range")
    #             return
    #         curr = curr.next
    #     node.next = curr.next
    #     curr.next = node

    # def remove_at_index(self, index):
    #     pass

    # def prepend(self, node):
    #     pass

    # def remove_head(self):
    #     # handle edge cases no head or only one node
    #     self.head = self.head.next

    def traverse(self):
        pass
