from data_structures.tree_binary import BinarySearchTree

#Implementnation using a recursive approach
def binary_search(sorted_list, left_pointer, right_pointer, target):
  
    if left_pointer >= right_pointer:
        return "value not found"

    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        # reduce the sub-list by passing in a new right_pointer
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        # reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


#Implementnation using a iterative approach
def binary_search(sorted_list, target):
    left_pointer = 0
    right_pointer = len(sorted_list)
  
    while right_pointer > left_pointer:
        mid_idx = (right_pointer + left_pointer) // 2
        mid_val = sorted_list[mid_idx]
        if mid_val == target:
            return mid_idx
        if target < mid_val:
            right_pointer = mid_idx
        if target > mid_val:
            left_pointer = mid_idx + 1
  
    return "Value not in list"


print("Creating Binary Search Tree rooted at value 15")
tree = BinarySearchTree(15)
print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()