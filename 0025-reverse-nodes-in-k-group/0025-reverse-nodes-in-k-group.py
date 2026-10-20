# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # STEP 1: Check if there are k nodes left to reverse
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Fewer than k nodes left, leave them alone!
            
            group_next = kth.next  # Save the rest of the list
            
            # STEP 2: The localized flip for these k nodes
            prev = group_next
            curr = group_prev.next
            
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # STEP 3: The handshakes (Stitching)
            tail = group_prev.next  # The old start is now our tail
            group_prev.next = kth   # Anchor connects to the new head (kth)
            group_prev = tail       # Move our anchor forward to this tail for the next group        