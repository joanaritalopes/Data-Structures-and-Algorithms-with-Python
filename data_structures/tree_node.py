# deque -> double-ended queue
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value # data
        self.children = [] # references to other nodes
    
    def __str__(self):
        stack = deque()
        stack.append([self, 0])
        level_str = " "
        while len(stack) > 0:
            node, level = stack.pop()
        
            if level > 0:
                level_str += " |" * (level-1) + "|-"
            level_str += str(node.value) + '\n '
            level+=1
            for child in reversed(node.children):
                stack.append([child, level])

        return level_str

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node) 
    
    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children 
                            if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children