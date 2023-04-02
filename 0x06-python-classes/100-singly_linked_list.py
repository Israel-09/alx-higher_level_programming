#!/usr/bin/python3
"""module to create a linked list"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return


    def print_list(self):
        current = self.head
        print(current.data)
        while current.next:
            print('{:d}'.format(current.data))
            current = current.next
            self.head = current


sll = SinglyLinkedList()
sll.insert_node(5)
sll.insert_node(5)
sll.insert_node(9)
sll.insert_node(1)
sll.insert_node(4)
sll.insert_node(4)
sll.print_list()
