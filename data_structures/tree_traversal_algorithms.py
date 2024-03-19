## Tree traversal algorithms

#Breadth-first search
def bfs(root_node, goal_value):

    # initialize frontier queue
    path_queue = queue()

    # add root path to the frontier
    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    # search loop that continues as long as
    # there are paths in the frontier
    while path_queue:
        # get the next path and node 
        # then output node value
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f"Searching node with value: {current_node.value}")

        # check if the goal node is found
        if current_node.value == goal_value:
            return current_path

        # add paths to children to the  frontier
        for child in current_node.children:
            new_path = current_path.copy()
            new_path.append(child)
            path_queue.appendleft(new_path)

    # return an empty path if goal not found
    return None


#Depth-first search
def dfs(root, target, path=()):
  path = path + (root,)

  if root.value == target:
    return path

  for child in root.children:
    path_found = dfs(child, target, path)

    if path_found is not None:
      return path_found

  return None