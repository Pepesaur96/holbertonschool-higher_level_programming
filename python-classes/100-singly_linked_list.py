#!/usr/bin/python3
"""This module contains a class Node that defines a node of a singly linked
list by:
-Private instance attribute: data
-Private instance attribute: next_node
-Instantiation with data and next_node
-Property getter and setter for data
-Property getter and setter for next_node"""


class Node:
    def __init__(self, data, next_node=None):
        """Initializes a new instance of the Node class with data and an
        optional next_node.
        Args:
            data: The data to be stored in the node (must be an integer).
            next_node: The next node in the singly linked list (must be
            a Node object or None).
        Raises:
            TypeError: If data is not an integer or next_node is not a
            Node object or None."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for the 'data' attribute.
        Returns:
            int: The data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for the 'data' attribute.
        Args:
            value: The new data value to set (must be an integer).
        Raises:
            TypeError: If value is not an integer."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for the 'next_node' attribute.
        Returns:
            Node: The next node in the singly linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for the 'next_node' attribute.
        Args:
            value: The new next_node value to set (must be a Node object or
            None).
        Raises:
            TypeError: If value is not a Node object or None."""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class with
        an empty list."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the entire singly linked list.
        Returns:
            str: The string representation of the list."""
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list
        (increasing order).
        Args:
            value: The value to insert into the list (must be an integer).
        Raises:
            TypeError: If value is not an integer."""
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return
