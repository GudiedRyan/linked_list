from main import Node, LinkedList

def test_node():
    node = Node(5)
    assert node.value == 5

def test_node_next():
    node = Node(5)
    assert node.next == None

def test_add_head():
    linked_list = LinkedList()
    linked_list.add_head(5)
    assert linked_list.head.value == 5

def test_add_head_next():
    linked_list = LinkedList()
    linked_list.add_head(5)
    linked_list.add_head(10)
    assert linked_list.head.value == 10

def test_add_after():
    linked_list = LinkedList()
    linked_list.add_head(43)
    linked_list.add_after(linked_list.head, 55)
    assert linked_list.head.next.value == 55

def test_add_end_empty():
    linked_list = LinkedList()
    linked_list.add_to_end(23)
    assert linked_list.head.value == 23

def test_search():
    linked_list = LinkedList()
    linked_list.add_head(5)
    linked_list.add_head(20)
    linked_list.add_to_end(15)
    assert linked_list.search(15) == True

def test_fail_search():
    linked_list = LinkedList()
    linked_list.add_head(123)
    assert linked_list.search(143) == False

def test_fail_delete():
    linked_list = LinkedList()
    assert linked_list.delete(10) == False
