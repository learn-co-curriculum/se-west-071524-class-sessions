import ipdb

from lib.linked_list import LinkedList
from lib.node import Node

if __name__ == "__main__":
    cloud_ll = LinkedList()
    cloud_ll.print()
    nimbus = Node("nimbus")
    cloud_ll.append(nimbus)
    stratus = Node("stratus")
    cloud_ll.append(stratus)
    cloud_ll.append(Node("cumulus"))
    cloud_ll.print()
