#!/usr/bin/python3
"""module to create a linked list"""


class Node:
    """defines a node"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__data

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            print(self.head.value)
"""        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
"""

    def __repr__(self):
        return self.list_order()

sll = SinglyLinkedList()
sll.sorted_insert(2)
#sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)


