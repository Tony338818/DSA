"""
A queue is a FIFO(First in First Out) Data struture. i.e what goes in first comes out first. 
Example :
a queue at a coffe shop, or a marching line

the uses of a queue is to process data as they come, following order.

The various operations of a queue includes:
enqueue -> Add more customers to the waiting line.
dequeue -> serve the frist customer in the line to they can leave.
peek -> check the first person in the queue.
isEmpty -> check the number of people in the line.
isFull -> the waiting area can only hold 5 people at a time, if a new person comes, sorry you can't wait in the line, checks the capacity of the line.
delete -> serve everyone in the queue or tell them we have no more coffee
create -> start a new line

Queues can be implemented using:
1. Python Lists.
2. LinkedLists.

There are also various types of queues:
1. Priority Queue -> where customers are served based on their importance.
2. 


There is also a circular linkedlist
"""

class Queue:
    def __init__(self):
        self.items = []
    
    # print the values of the queue
    def __str__(self):
        return ' '.join(str(x) for x in self.items) if self.items else 'Empty'
        
    # check the number of people in the line
    def isEmpty(self):
        return len(self.items) == 0
    
    # add people to the queue
    def enqueue(self, value):
        self.items.append(value)
        return 'new customer has joined the queue'
    
    # serve people so they can leave
    def dequeue(self):
        if self.isEmpty():
            return 'queue is empty'
        
        val = self.items.pop(0)
        return f'Customer {val} served'
    
    # check the first person on the line
    def peek(self):
        return self.items[0]
    
    # clear the line
    def delete(self):
        self.items = None
        return 'No customer on the line'
    
testQueue = Queue()
testQueue.enqueue(1)
testQueue.enqueue(2)
testQueue.enqueue(3)
print(f'Initial queue {testQueue}')
print(testQueue.isEmpty())
testQueue.dequeue()
print(f'after dequeue {testQueue}')
print(f'peeking {testQueue.peek()}')
testQueue.delete()
print(f'after delete {testQueue}')



# Circular Queues
class CircularQueue:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.start = -1
        self.top = -1