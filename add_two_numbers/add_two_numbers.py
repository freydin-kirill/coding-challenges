from typing import Optional


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if either l1 or l2 is None. If one of them is None, return the other linked list.
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # Create a new linked list to store the result
        ans = ListNode()
        node = ans  # Initialize a pointer to the head of the result linked list
        value, extra = 0, 0  # Initialize variables to store the sum and carry (extra)

        # Loop until both l1 and l2 are None and there is no carry (extra) left
        while l1 is not None or l2 is not None or extra:
            # Calculate the sum of the current nodes' values and the carry (extra)
            value = extra
            if l1 is not None:
                value += l1.val
                l1 = l1.next
            if l2 is not None:
                value += l2.val
                l2 = l2.next

            # Calculate the new carry (extra) for the next iteration
            extra = value // 10

            # Create a new node with the value (sum % 10) and append it to the result linked list
            node.next = ListNode(value % 10)
            node = node.next  # Move the pointer to the newly created node

        return ans.next  # Return the head of the result linked list (skip the dummy first node)
