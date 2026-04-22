"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def add_two_numbers(l1: Node, l2: Node):
    new_list = Node(0)
    current = new_list
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
        