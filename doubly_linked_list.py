class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def add_head(self, value):
        new_head = Node(value)
        new_head.next = self.head
        new_head.previous = None
        self.head = new_head

    def add_to_end(self, value):
        if self.head == None:
            self.add_head(value)
            return
        new_node = Node(value)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.previous = current_node

    def find_node(self, value):
        if self.head == None:
            return False
        elif self.head.value == value:
            return self.head
        current_node = self.head
        while current_node.value != value:
            if current_node.next == None:
                return False
            current_node = current_node.next
        return current_node
    
    def search_list(self, value):
        if self.head == None:
            return False
        elif self.head.value == value:
            return self.head.value
        current_node = self.head
        while current_node.value != value:
            if current_node.next == None:
                return False
            current_node = current_node.next
        return current_node.value