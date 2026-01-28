"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class LinkedList():
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
 
class Solution():       
    def add_two_numbers(self, l1: LinkedList, l2: LinkedList):
        start = LinkedList(0)
        current = start
        carry = 0
        
        while l1 or l2 or carry:
            sum = carry
            
            if l1:
                sum += l1.value
                l1 = l1.next
            if l2:
                sum += l2.value
                l2 = l2.next
                
            carry = sum // 10
            current.next = LinkedList(sum % 10)
            current = current.next

        return start.next
    
def build_list(values):
    head = None
    for v in reversed(values):
        head = LinkedList(v, head)
    return head

l1 = build_list([2, 4, 3])
l2 = build_list([5, 6, 4])

def print_list(node):
    values = []
    while node:
        values.append(str(node.value))
        node = node.next
    print(" -> ".join(values))
 
    
solution = Solution()
print_list(solution.add_two_numbers(l1, l2))