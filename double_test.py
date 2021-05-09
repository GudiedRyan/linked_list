from doubly_linked_list import Node, DoublyLinkedList

def test_node():
    node = Node(23)
    assert node.value == 23

def test_add_head():
    double_link_list = DoublyLinkedList()
    double_link_list.add_head(24)
    double_link_list.add_head(35)
    assert double_link_list.head.value == 35 and double_link_list.head.next.value == 24

def test_search_fail():
    dllist = DoublyLinkedList()
    dllist.add_head(55)
    dllist.add_head(1)
    dllist.add_head(98)
    dllist.add_head(67)
    assert dllist.search_list(4) == False

def test_search_pass():
    dllist = DoublyLinkedList()
    dllist.add_head(55)
    dllist.add_head(1)
    dllist.add_head(98)
    dllist.add_head(67)
    assert dllist.search_list(98) == 98

def test_find_node():
    dllist = DoublyLinkedList()
    dllist.add_head(123)
    dllist.add_head(67)
    assert dllist.find_node(123) == dllist.head.next

def test_add_to_end_empty():
    dllist = DoublyLinkedList()
    dllist.add_to_end(45)
    assert dllist.head.value == 45

def test_add_to_end():
    dllist = DoublyLinkedList()
    dllist.add_to_end(34)
    dllist.add_to_end(67)
    assert dllist.find_node(67).previous.value == 34