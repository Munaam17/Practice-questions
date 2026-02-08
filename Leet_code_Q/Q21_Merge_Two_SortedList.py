# Leetcode Problem: Merge Two Sorted List

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        # Create a dummy node to simplify edge cases
        dummy = ListNode()
        cur = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1       # Attach list1's node
                list1 = list1.next     # Move list1 pointer
            else:
                cur.next = list2       # Attach list2's node
                list2 = list2.next     # Move list2 pointer

            cur = cur.next             # Move cur to last node

        # Attach the remaining nodes if one list is not empty
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        # Return the merged list, skipping dummy
        return dummy.next
    
# ----------------- Internal call -----------------
# Create lists
list1 = ListNode(1, ListNode(5, ListNode(8, ListNode(8))))
list2 = ListNode(1, ListNode(3, ListNode(4, ListNode(9))))

# Call the function
solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

# Directly print the merged list
cur = merged
while cur:
    print(cur.val, end=" -> " if cur.next else "")
    cur = cur.next
    
