class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
            # node will start as self.head and prev will start as None
            # loop through the entire list
            while node:                           
                temp_next = node.next_node # save the next node before we move its pointer and lost track of it
                node.next_node = prev # flip the pointers direction in the list
                # iterate prev and cur variables by 1 each
                prev = node
                node = temp_next
            # after loop finishes and all pointers are reversed
            # set head to old tail, which will be the prev
            self.head = prev
        
