"""
This module defines a basic Node class for implementing a various data structures, 
such as LinkedLists, Queues, Stacks, ...
"""

class Node:
    """
    This class represents a node with a value (data) and a pointer (reference) to the next node.
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_value(self):
        return self.value