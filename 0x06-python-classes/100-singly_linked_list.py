#!/usr/bin/python3

"""A singly linked link Build"""

class Node:
    """Creating a Node Class"""

    def __init__(self, data, next_node=None):
        """Initialization method"""
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if isinstance(next_node, Node) or next_node == None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Retrieving data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Retrieving next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node"""
        if isinstance(value, Node) or value == None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """A Singly Linked List Class"""

    def __init__(self):
        """initialization method"""
        self.__head = None

    def sorted_insert(self, value):
        """add and sort the head"""
        new_node = Node(value)
        if self.__head is None or value < self.__head.__data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.__next_node is not Node:
                current = current.__next_node
            new_node.next_node = current.__next_node
            current.__next_node = new_node

    def __str__(self):
        """print out the values in head"""
        result = []
    current = self.head
    while current:
        result.append(str(current.data))
        current = current.next_node
    return "\n".join(result)
