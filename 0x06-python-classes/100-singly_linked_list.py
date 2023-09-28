#!/usr/bin/python3

"""A singly linked list build"""


class Node:
    """Creating  a Node class
    """

    def __init__(self, data, next_node=None):
        """Initialization Method"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieving Data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Settin Data"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieving next_node"""
        return self.__next_node

    @data.setter
    def next_node(self, value):
        """Setting next_node"""
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A singly linked list class"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """add and sort to the head
        """
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
    """print out the values in the head"""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
