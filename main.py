class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def add_after(self, prev_node, value):
        if prev_node is None:
            print("prev node not in list")
            return
        added_node = Node(value)
        added_node.next = prev_node.next
        prev_node.next = added_node

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last.next = new_node

    def search(self, value):
        if self.head == None:
            return False
        elif self.head.value == value:
            return self.head.value
        current_node = self.head
        while current_node.value != value:
            if current_node.next == None:
                return False
            current_node = current_node.next
        return True

    def delete(self, value):
        if self.search(value):
            current_node = self.head
            prev_node = None
            if self.head.value == value:
                temp_head = self.head.next
                self.head = None
                self.head = temp_head
                return
            while current_node.value != value:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = current_node.next
            print(f"Node {current_node.value} has been deleted")
            current_node = None
            return     
        print("Value not in list")
        return False

    def print_nodes(self):
        if self.head == None:
            print("Linked list has no nodes")
            return True
        current_node = self.head
        while current_node.next != None:
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)
        return current_node.value