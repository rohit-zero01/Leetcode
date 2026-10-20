# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # Base case: if list is empty or has only one node, nothing to swap
        if not head or not head.next:
            return head

        # Step 1: Create a dummy node anchor
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 2: Loop as long as there is a pair of nodes ahead to swap
        while prev.next and prev.next.next:
            # Identify our pair
            first = prev.next
            second = prev.next.next

            # Step 3: The 3-Step Choreography
            # 1. Save the future (the rest of the train after the pair)
            rest = second.next

            # 2. Flip the pair
            second.next = first
            first.next = rest

            # 3. Connect the anchor (prev) to the new front of this pair
            prev.next = second

            # Advance prev to the end of this swapped pair for the next round
            prev = first

        return dummy.next


        