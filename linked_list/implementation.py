from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start=None
        self.end=None
        if elements:
            for e in elements:
                self.append(e)

    def __str__(self):
        return "[{}]".format(', '.join([str(e) for e in self]))

    def __len__(self):
        return self.count()

    def __iter__(self):
        """ use generators here to return the linkedlist"""
        n = self.start
        while n:
            yield n.elem
            n=n.next
        raise StopIteration

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        for i,e in enumerate(self):
            if i==index:
                return e

    def __add__(self, other):
        new_list = self.__class__([elem for elem in self])
        for e in other:
            new_list.append(e)
        return new_list

    def __iadd__(self, other):
        for e in other:
            self.append(e)
        return self

    def __eq__(self, other):
        a = self.start
        b = other.start
        while True:
            if not a and not b:
                return True
            #if either are None - they don't match
            if not bool(a) or not bool(b):
                return False
            
            #check value
            if a.elem != b.elem:
                return False
            a = a.next
            b = b.next

    def append(self, elem):
        """
        Only set start if not set otherwise set the next value to the current 'end' to elem and 
        set end to elem
        """
        if self.start is None:
            self.start = Node(elem)
            self.end = self.start
            return self.start
        n = Node(elem)
        self.end.next = n
        self.end=n
        
        
    def count(self):
        """
        counter for length
        """
        cnt=0
        for e in self:
            cnt+=1
        return cnt

    def pop(self, index=None):
        """
        1 - validate the index value passed
        2 - if index==0 then just move the start
        3 - else iterate through the list until the index
        """
        cnt = self.count()
        if index is None:
            index=cnt-1
        if index >= cnt:
            raise IndexError
        if cnt==0:
            raise IndexError
        
        if index==0:
            #remove the first element and reassign the start to the next of current start
            val = self.start.elem
            self.start = self.start.next
            return val
        n=0
        prev=None
        curr= self.start
        while True:
            if n==index:
                prev.next=curr.next
                return curr.elem
            #swap and go up the chain
            prev=curr
            curr=curr.next
            n+=1
            
    def __ne__(self,other):
        return not self.__eq__(other)
            
