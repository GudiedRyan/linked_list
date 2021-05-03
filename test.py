from main import Node, LinkedList

def test_node():
    node = Node(5)
    assert node.value == 5

def test_node_next():
    node = Node(5)
    assert node.next == None

def test_add_head():
    linked_list = LinkedList()
    linked_list.add(5)
    assert linked_list.head.value == 5

def test_add_head_next():
    linked_list = LinkedList()
    linked_list.add(5)
    linked_list.add(10)
    assert linked_list.head.value == 10