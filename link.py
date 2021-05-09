from main import Node, LinkedList

link = LinkedList()
link.add_head(33)
link.add_to_end(45)
link.add_after(link.head, 2)
#link.print_nodes()
link.delete(33)
#link.print_nodes()

link2 = LinkedList()
link2.add_head(4)
link2.update_node(link2.head,5)
link2.print_nodes()