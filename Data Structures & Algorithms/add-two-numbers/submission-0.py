# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1!=None or l2!=None or carry!=0:
            l1Value = l1.val if l1 else 0
            l2Value = l2.val if l2 else 0
            currentSum = l1Value+l2Value+carry
            carry = currentSum//10
            newNode = ListNode(currentSum%10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        