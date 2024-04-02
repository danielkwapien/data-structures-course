from slistH import SList
from slistH import SNode

import sys


class SList2(SList):

    def delLargestSeq(self):
        node = self._head
        prev = None
        first = None
        last = None
        count_max = 1
        while node:
            count = 1
            while node.next and node.elem == node.next.elem:
                count += 1
                node = node.next
            if count >= count_max:
                count_max = count
                first = prev
                last = node
            prev = node
            node = node.next

        if not first:
            self._head = last.next
        else:
            first.next = last.next
        self._size -= count_max

    def fix_loop(self):
        slow = fast = self._head
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self._head
                if slow == fast:
                    prev.next = None
                    return True
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next
                fast.next = None
                return True
        return False

    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next
        current.next = start_node

    def leftrightShift(self, left, n):
        if self._size == 0 or n >= self._size:
            return
        prev = None
        node = self._head
        current = self._head
        if not left:
            n = self._size - n
        while n != 0:
            n -= 1
            prev = current
            current = current.next
        prev.next = None
        self._head = current
        while current.next:
            current = current.next
        current.next = node


l = SList2()
[l.addLast(i) for i in [1, 2, 3]]
l.create_loop(0)
output = l.fix_loop()
print(l)
if __name__ == '__main__':

    '''l = SList2()
    for i in [1,2,3,4,5]:        
        l.addLast(i)
    print(l.delLargestSeq())


    l=SList2()
    for i in range(7):
         l.addLast(i+1)

    print(l)
    l.leftrightShift(False, 2)
    print(l)'''




