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
                    sum += (l1.val * (10 * zeroC))
                    zeroC = 0
                    zeroSeen = False
                else:
                    sum1 += l1.val * i
            else:
                zeroC += 1
            i *= 10
            l1 = l1.next

        while l2 != None:

            if l2.val != 0:
                if zeroSeen:
                    sum += (l2.val * (10 * zeroC))
                    zeroC = 0
                    zeroSeen = False
                else:
                    sum2 += l2.val * i
            else:
                zeroC += 1
            k *= 10
            l2 = l2.next
        print
        sum1
        print
        sum2
        total = str(sum1 + sum2)[::-1]
        k = ListNode(0, None)
        h = k
        for integer in range(0, len(total)):
            if integer != len(total):
                k.next = ListNode(int(total[integer]), None)
                print
                k.next
                k = k.next
        print
        k
        return h.next

        00002

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
