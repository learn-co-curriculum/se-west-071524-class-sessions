import ipdb

from lib.linked_list import LinkedList
from lib.node import Node

if __name__ == "__main__":
    cloud_ll = LinkedList()
    cloud_ll.find("cumulus")
    cloud_ll.print()
    nimbus = Node("nimbus")
    cloud_ll.append(nimbus)
    stratus = Node("stratus")
    cloud_ll.append(stratus)
    cloud_ll.append(Node("cumulus"))
    cloud_ll.print()
    target = cloud_ll.find("nimbus")
    print(target)
    print(cloud_ll.find("cirrus"))
    cirrus = Node("cirrus")
    cloud_ll.insert_after(target, cirrus)
    cloud_ll.print()
    lent = Node("lenticular")
    cloud_ll.insert_at_index(2, lent)
    cloud_ll.print()
    cloud_ll.insert_at_index(6, Node("cumulonimbus"))
    cloud_ll.print()
