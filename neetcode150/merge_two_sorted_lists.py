"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1: Node, l2: Node):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = Node(0)
        current = new_list

        
        while l1 and l2:
            if l1.value <= l2.value:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
        
            current = current.next
        current.next = l1 if l1 else l2
        
        return new_list.next.value
    
node1 = Node(1)
node3 = Node(3)
node5 = Node(5)

node2 = Node(2)
node4 = Node(4)
node6 = Node(6)

node1.next = node3
node3.next = node5
node5.next = None

node2.next = node4
node4.next = node6
node6.next = None


sol = Solution()
result = sol.mergeTwoLists(l1=node1, l2=node2)
print(result)