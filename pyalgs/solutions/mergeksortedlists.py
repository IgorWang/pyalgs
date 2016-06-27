#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by igor on 16-6-27
'''
Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list.
'''

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next is None:
            return repr(self.val)
        else:
            return repr(self.val) + "->" + repr(self.next)

class Solution(object):
    def mergeKLists(self,lists):
        '''
        :param lists: List[ListNode]
        :return: ListNode
        '''
        if len(lists) == 0:
            return None
        def loop(lists,lo,hi):
            if lo > hi :
                return None
            if hi - lo == 1:
                return lists[lo]
            elif hi - lo == 2:
                return self.mergeHiper(lists[lo],lists[hi-1])
            else:
                mid = (lo + hi) // 2
                return self.mergeHiper(loop(lists,lo,mid),loop(lists,mid,hi))
        return loop(lists,0,len(lists))

    def mergeHiper(self,N1,N2):
        head = ListNode(0)
        p = head
        while N1 is not None and N2 is not  None:
            if N1.val <= N2.val:
                p.next = ListNode(N1.val)
                N1 = N1.next
            else:
                p.next = ListNode(N2.val)
                N2 = N2.next
            p = p.next

        if N1 :
            p.next = N1
        elif N2:
            p.next = N2

        return head.next

if __name__ == '__main__':
    #TEST mergeHiper
    l1 = ListNode(3)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(4)
    l2.next = ListNode(8)
    l2.next.next = ListNode(10)
    print(l1)
    print(l2)

    s = Solution()
    l3 = s.mergeHiper(l1,l2)
    print(l3)

    print(s.mergeKLists([l1,l2]))

