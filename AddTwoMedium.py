# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        i = 1
        k = 1
        sum1 = 0
        sum2 = 0
        zeroSeen = False
        zeroC = 0
        while l1 != None:
            if l1.val != 0:
                if zeroSeen:
                    sum1 += (l1.val * i)
                    zeroC = 0
                    zeroSeen = False
                else:
                    sum1 += l1.val * i
            else:
                zeroC += 1
                zeroSeen = True
            i *= 10
            l1 = l1.next

        while l2 != None:

            if l2.val != 0:
                if zeroSeen:
                    sum2 += (l2.val * (k))
                    zeroC = 0
                    zeroSeen = False
                else:
                    sum2 += l2.val * k
            else:
                zeroC += 1
                zeroSeen = True
            k *= 10
            l2 = l2.next
        total = str(sum1 + sum2)[::-1]
        k = ListNode(0, None)
        h = k
        for integer in range(0, len(total)):
            if integer != len(total):
                k.next = ListNode(int(total[integer]), None)
                print
                k.next
                k = k.next
        return h.next

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
