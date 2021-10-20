#The objective of this activity is to implement a stack,trying to solve
#the problem by thinking about objects. with the next constraints

#top: returns the element that is at the top of the stack.
#push: Stack a new item.
#pop: Unstack an item and return it. Raise an exception if an empty stack is popped.
#len: Returns the number of elements in the stack.
#is_empty: Indicates if the stack is empty.

class EmptyStack(Exception):
    pass
# stack representation
class Stack(object):
    
    def __init__(self):
        self.head = StackBase()

    def top(self):
        return self.head

    def push(self, value):
        self.head = self.head.push(value)

    def pop(self):
        old_head = self.head
        self.head = self.head.pop()
        return old_head

    def len(self):
        return self.len.head()

    def is_empty(self):
        return self.head.is_empty()

#base representation
class StackBase(object):
    
    def push(self, value):
        return StackItem(parent=self, value=value)
    
    def pop(self):
        raise EmptyStack("Stack empty") 

    def len(self):
        return 0

    def is_empty(self):
        return True

#represent 1 item of the stack
class StackItem(object):

    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

    def push(self, value):
        return StackItem(parent=self, value=value)

    def pop(self):
        return self.parent

    def len(self):
        return self.parent.len + 1

    def is_empty(self):
        return False

    def __repr__(self):
        return 'Stack base'



#intances
stack = Stack()
stack.push(1)
stack.push(2)
stack.top()
stack.pop()
stack.pop()
stack.pop()
stack.push(2)
stack.push(3)
stack.len()
stack.is_empty()