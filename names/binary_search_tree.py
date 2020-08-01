"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if tree is empty make value = root
        if self.value is None:
            self.value = BSTNode(value)       
        # compare to the new value we want to insert        
        # if new value <= self.value
        
        elif value < self.value:
            # IF self.left is already taken by a node
            if self.left is None:
            # set the left to the new node with the new value
                self.left = BSTNode(value)
            else:
                # make that (left) node call insert
                self.left.insert(value)
            
        # if new value > self.value
        elif value >= self.value:
            # IF self.right is already taken by a node
            if self.right is None:
            # set the right child to the new node with new value (update current node to be current_node.right)
                self.right = BSTNode(value)        
            else:
                # make that (right) node call insert
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # end goal - if target is equal to the root node
        if self.value == target:
            return True
        # compare the target to current value 
        if target < self.value:
            # check the left subtree
            # if you cannot go left, return False
            if self.left is None:
                return False
            # if there is a left node, make that node call contains
            return self.left.contains(target) # use recursion to return True or False
        # if current value > target
        if target >= self.value:
            #check if right subtree contains target
            # if you cannot go right return False
            if self.right is None:
                return False
            # if there is a right node, make that node call contains
            return self.right.contains(target) # use recursion to return True or False

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will be on the bottom right of our tree
        # When there is no more right trees, return the current node's value (MAX)
        if self.right is None:
            return self.value           
        # go right if you can
        return self.right.get_max()
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value fn(self.value)
        fn(self.value)
        # if left node then call for_each on it
        if self.left is not None:
            self.left.for_each(fn)
        # if right node call for_each on it
        if self.right is not None:
            self.right.for_each(fn)
            
    def delete(self, value):
        pass
        # search for value like we did in contains()
        
        # cases
        # if node at bottom level
            # update parent left/right = None
        # if node is an only child
            # parent.left/right = node.left/right
        # if node has 2 children
            # larger child becomes the parent of its sibling
        
    # Part 2 -----------------------
 
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self:            
            if self.left is not None:
                # go left
                self.left.in_order_print(self.left)
                
            # print current node
            print(self.value)
            
            if self.right is not None:
                # go right
                self.right.in_order_print(self.right)
            #print
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = Queue()
        # add the first node to the queue
        queue.enqueue(node)
        # while queue is not empty
        while queue.size > 0:
            # remove the first node from the queue
            removed = queue.dequeue()
            # print the removed node
            print(removed.value)
            # add all children into the queue
            if removed.left:
                queue.enqueue(removed.left)
            if removed.right:
                queue.enqueue(removed.right)     

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        stack = Stack()
        # add the first node to the stack
        stack.push(node)
        # while the stack is not empty
        while stack.size > 0:
            # get the current node from the top of the stack - pop
            removed = stack.pop()
            # print that node
            print(removed.value)
            # add all children to stack - order matters!
            if removed.left:
                stack.push(removed.left)
            if removed.right:
                stack.push(removed.right)
        # done when stack is empty

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.in_order_print(bst)
bst.bft_print(bst)
bst.dft_print(bst)

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
