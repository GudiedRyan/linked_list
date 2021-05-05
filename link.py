from main import Node, LinkedList

link = LinkedList()
link.add_head(33)
link.add_to_end(45)
link.add_after(link.head, 2)
link.print_nodes()
link.delete(33)
link.print_nodes()