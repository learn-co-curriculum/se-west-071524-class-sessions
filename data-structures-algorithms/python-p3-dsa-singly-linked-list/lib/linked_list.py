class LinkedList:
    def __init__(self, head=None):
        self.head = head

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
        pass

    def insert_after(self, target_node, new_node):
        pass

    def insert_at_index(self, index, node):
        pass
