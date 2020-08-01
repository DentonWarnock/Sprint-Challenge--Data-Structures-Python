"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # if list is empty
        if self.head is None and self.tail is None:
            #set the head and tail to equal the new node
            self.head = new_node
            self.tail = new_node
        else:
            # the list has elements
            # make new node's value point to current head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # if list is empty
        if self.head is None and self.tail is None:
            #set the head and tail to equal the new node
            self.head = new_node
            self.tail = new_node
        else:
            # the list has elements
            # make new node's value point to current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return        
        # save the value we will deleted
        old_value = node.value
        # delete
        self.delete(node)
        # add_to_head(value)
        self.add_to_head(old_value)
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return        
        # save the value we will delete
        old_value = node.value
        # delete
        self.delete(node)
        # add_to_head(value)
        self.add_to_tail(old_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):     
        # the list is empty -> do nothing
        if self.head is None and self.tail is None:
            return
        # the list is only one node
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        # the node is the HEAD node
        elif self.head == node:
            self.head = node.next
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        # the node is the TAIL node
        elif self.tail == node:
            self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        # the node is just some node in the list  
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        #empty list
        if self.head is None:
            return None
        # non-empty list
        # iterate through all items
        current_node = self.head
        current_max = self.head.value
        while current_node is not None:
            if current_node.value > current_max:
                current_max = current_node.value
                
            #iterate
            current_node = current_node.next
            
        return current_max