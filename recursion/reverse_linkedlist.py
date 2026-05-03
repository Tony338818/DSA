"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class SLL:    
    def reverseLinkedlist(self, head: Node):
        # base case
        if head is None or head.next is None:
            return head
        
        # reverse the rest
        new_head = self.reverseLinkedlist(head.next)
        
        # fix current node
        head.next.next = head
        head.next = None
        
        return new_head
  

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)  

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

sll = SLL()
result = sll.reverseLinkedlist(node1)
print(result.value)
        
        