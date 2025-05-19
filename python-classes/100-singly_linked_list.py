#!/usr/bin/python3
'''
This module provides 2 classes to manipulate singly linked lists
'''


class Node:
    '''
    This class defines a node for a singly linked list

    Args:
        data (int): The data of the node.
        next_node (Node): The next node of the list
    '''
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''
        The getter for data
        '''
        return self.__data

    @property
    def next_node(self):
        '''
        The getter for next_node
        '''
        return self.__next_node

    @data.setter
    def data(self, value):
        '''
        The setter for the data

        Args:
            value (int): The value of the data
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @next_node.setter
    def next_node(self, value):
        '''
        The setter for next_node

        Args:
            value (Node): The next_node.
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    '''
    This class create a singly linked list
    '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        '''
        This method will insert a new node in the list and sort
        it by value.

        Args (int): The value of the data inside the node.
        '''
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        '''
        This method make it possible to print the list in stdout
        with one data by line.
        '''
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
