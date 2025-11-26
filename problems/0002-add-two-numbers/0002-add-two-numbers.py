# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode(0)#init 
        answernode = result# builds the linked list from result node
        carry = 0
        p, q = l1, l2
        while p or q or carry:
            #values in case one list longer than the other
            x = p.val if p else 0
            y = q.val if q else 0
            current = x + y + carry
            carry = current // 10 #anything above below 10 becomes 0
            answernode.next = ListNode(current % 10)
            #push to next loop
            answernode=answernode.next
            if p: p = p.next
            if q: q = q.next
        return result.next #result list build whilst never moving the node

# mod 10 the numbers after adding them
#return the sum in a linked list