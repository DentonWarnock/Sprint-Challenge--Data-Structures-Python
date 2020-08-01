from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.oldest = None
        
    # use FIFO method with DLL
    def append(self, item):
        # if length of storage is less than capacity - add the item to tail
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        # otherwise storage == capacity --> replace oldest item with new item
        else:
            # check if oldest == None --> if so make oldest = head
            if self.oldest is None: # default condition
                self.oldest = self.storage.head
            # set oldest item to new item
            self.oldest.value = item
            # set next item in DLL to new oldest item
            self.oldest = self.oldest.next
            
    def get(self):
        contents = [] # empty list container
        cur = self.storage.head # starting point for loop
        # Loop through DLL contents
        while cur is not None:
            # add each element
            contents.append(cur.value)
            # iterate through loop
            cur = cur.next
        # return contents
        return contents