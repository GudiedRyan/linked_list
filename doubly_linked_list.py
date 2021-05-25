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

    def delete_node(self,value):
        if self.head == None:
            return False
        elif self.head.value == value:
            if self.head.next == None:
                self.head = None
                return True
            self.head.next.previous = None
            self.head.next = self.head
            return True
        current_node = self.head
        while current_node.value != value:
            if current_node.next == None:
                return False
            current_node = current_node.next
        if current_node.next == None:
            current_node.previous.next = None
            current_node = None
            return True
        current_node.previous.next = current_node.next
        current_node.next.previous = current_node.previous
        current_node = None
        return True

    def add_after(self, prev: Node, value):
        if prev == self.head:
            self.insert(prev_node=self.head, value=value)
            return True
        current = self.head
        while current != prev:
            current = current.next
        if current.next == None:
            self.add_to_end(value)
        else:
            self.insert(prev_node=current, value=value)

    def insert(self, prev_node: Node, value):
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next.previous = new_node
        prev_node.next = new_node
        new_node.previous = prev_node
