# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=0
        temphead=head
        while temphead.next!=None:
            temp+=1
            temphead=temphead.next
        for n in range(-(-temp//2)):
            head=head.next
        return head