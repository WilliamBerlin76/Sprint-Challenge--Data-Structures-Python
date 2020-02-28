from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity - 1:
            self.storage.add_to_tail(item)
            self.current = 'pass'
        elif self.storage.length < self.capacity - 1:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail 

        elif self.storage.length == self.capacity and self.current is 'pass':
           
            self.storage.head.value = item
            self.current = self.storage.head.next
        elif self.storage.length == self.capacity and self.current.next is None:
            
            self.storage.tail.value = item
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            
            self.storage.replace(self.current, item)
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        temp = self.storage.head
        while temp is not None:
            list_buffer_contents.append(temp.value)
            temp = temp.next
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
