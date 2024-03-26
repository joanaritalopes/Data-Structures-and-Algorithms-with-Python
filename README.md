# Data Structures and Algorithms with Python
Small projects to learn about data structures and algorithms using Python:

### Stacks: Towers of Hanoi
- Towers of Hanoi is an ancient mathematical puzzle that starts with three stacks and many disks.
- The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.
- The game follows three rules: (1) Only one disk can be moved at a time (2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod (3) No disk may be placed on top of a smaller disk.
- The number of optimal moves is always 2^Number of Disks - 1

### Hash Maps: Blossom
- In this project, we implement a hash map to relate the names of flowers to their meanings.
- To avoid collisions when our hashing function collides the names of two flowers, separate chaining for collision resolution is used.
- A collision occurs when two different keys hash to the same index in the underlying array. Instead of overwriting the existing value or finding a different slot, we implement the Linked List data structure at each array index for each of these separate chains. The linked list stores all key-value pairs that hash to the same index, allowing multiple entries to coexist in the same slot. This approach ensures that multiple key-value pairs that hash to the same index can be stored and retrieved without conflicts.

### Recursion: Fibonacci
- Fibonacci numbers are integers that follow a specific sequence: the next Fibonacci number is the sum of the previous two Fibonacci numbers.
- The Fibonacci Sequence starts with 0 and 1 respectively. If the function receives an input in that range, there is no need to do any work. If it receives an input > 1, the recursive step requires two previous Fibonacci numbers to calculate the current Fibonacci number and, therefore, the function will need two recursive calls in the recursive step.

### Trees: Make Your Own Wilderness Escape Story
- Make a unique story experience by allowing the player to pick the next chapter of their adventure. 
- This project uses a tree data structure to keep track of the different paths a user may choose. A TreeNode class keeps track of two things: (1) a portion of the story and (2) the choices a user can make to progress in the story.

### Graphs: Build a Route Planning Tool to Help Commuters
- Create a program to help commuters get from one landmark to another by metro. We build a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this.
- For the purpose of this project, we assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.

### Graphs and Heaps: Traveling Salesperson
- Find the shortest path that will allow to visit each city once, finishing at the city in which the journey started. This is a graph theory problem that is solved by using a Greedy Algorithm, algorithm usually used in optimization problems.
- For the purpose of this project, the objective is to apply the same implementation of Dijkstra’s Algorithm that finds the path with the minimum cost from one vertex to the others in a graph. The algorithm finds such a path by always going to the nearest vertex. That's why it is a greedy algorithm.