# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        # nums = []
        # current = head

        # while current:
        #     nums.append(current.val)
        #     current = current.next
        # # return nums

        # curr_max = -1
        # new_nums = []

        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i]>=curr_max:
        #         curr_max = nums[i]
        #         new_nums.append(nums[i])

        # new_nums.reverse()

        # dummy = ListNode(0)
        # current = dummy
        # for val in new_nums:
        #     current.next = ListNode(val)
        #     current = current.next

        # return dummy.next
        
        stack = []
        curr = head

        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]

        stack[-1].next = None

        return stack[0]

        