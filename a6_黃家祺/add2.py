"""
File: add2.py
Name:Cindy Huang
------------------------
This function takes 2 non-empty linked lists and sum the digits together
in reversed order, returning the sum as a new linked list
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    This function sums the digits in l1 and l2 and return the answer as a new ListNode
    :param l1: ListNode of l1
    :param l2: ListNode of l2
    :return: new ListNode with the sum of the digits in l1 and l2
    """
    # create empty ListNode to store answer
    answer = ListNode()
    # Position to insert new digit into
    cur = answer
    # integer used to store carried over values when sum of l1 + l1 exceeds 9
    carry_value = 0
    # check to see if l1 or l2 or carry_value is not None
    while l1 or l2 or carry_value:
        if l1 is not None:
            # assign l1 digit to value_1
            value_1 = l1.val
        # assign 0 as placeholder if l1 does not have a value
        else:
            value_1 = 0

        if l2 is not None:
            # assign l2 digit to value_2
            value_2 = l2.val
        # assign 0 as placeholder if l2 does not have a value
        else:
            value_2 = 0

        # Compute new digit as new_value
        new_value = value_1 + value_2 + carry_value
        # Obtain carried over value to add to next value when l1+l2 is greater than 10
        carry_value = new_value // 10
        # Get unit one's place digit
        new_value = new_value % 10
        # insert new ListNode
        cur.next = ListNode(new_value)

        # update pointers
        cur = cur.next
        if l1 is not None:
            l1 = l1.next
        else:
            l1 = None
        if l2 is not None:
            l2 = l2.next
        else:
            l2 = None

    return answer.next


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
