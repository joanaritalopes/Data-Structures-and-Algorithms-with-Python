from data_structures.node import Node
from data_structures.linked_list import LinkedList

class HashMap:
    """
    Implements a basic hash map data structure which allows the storage of key-value pairs.
    This class represents a basic HashMap data structure using separate chaining for collision resolution by using linked lists at each array index.
    """
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for item in range(size)]

    #Internal methods needed to perform the basic responsibilities of a hash map
    def hash(self, key):
        """
        Computes a hash code for a given key.
        """
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    #External methods to interact with the hash map
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if key == item[0]:
                item[1] = value
                return 
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if key == item[0]:
                return item[1]
        return None


flower_definitions = [
    ['daisy', 'innocence'], 
    ['rose', 'love'], 
    ['sunflower', 'longevity']
    ]

#Create the instance
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

#Try it out
print(blossom.retrieve('daisy'))