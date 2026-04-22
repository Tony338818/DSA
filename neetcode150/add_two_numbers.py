"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def addTwoNumbers(l1: Node, l2: Node):
    list_sum = Node(0)
    current = list_sum
    carry = 0
    
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.value
            l1 = l1.next
        if l2:
            total += l2.value
            l2 = l2.next
        
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next
    
    return list_sum.next.value

node1 = Node(2)
node2 = Node(4)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = None

node4 = Node(5)
node5 = Node(6)
node6 = Node(4)

node4.next = node5
node5.next = node6
node6.next = None

result = addTwoNumbers(node1, node4)
print(result)
