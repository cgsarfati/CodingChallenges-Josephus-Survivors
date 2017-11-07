"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""

# Plan:
    # Need a circular linked list (last item circles back to beginning)
    # Actions:
        # Add node - use 1st param to initialize LL
        # Traversal - use 2nd param to know how many times to jump
        # Remove node
    # Considerations:
        # Do we need to remove node? Or just find a way to mark it?
        # Circular traversal ends when LL only has 1 node left?


class Node(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    @classmethod
    def make_list(cls, n):
        """Construct circular doubly-linked list of n items. Returns head node.

            >>> node = Node.make_list(3)

            >>> node.data
            1

            >>> node.next.data
            2

            >>> node.next.next.next.data
            1

            >>> node.prev.data
            3

            >>> node.prev.prev.prev.data
            1
        """

        # Make 1st node (+ remember that it's the first for later)
            # Side-note: can do multiple-assignments in python!
        first = node = prev = cls(1)

        # Make every other node
        for i in range(2, n + 1):
            node = Node(i, prev=prev)
            prev.next = node
            prev = node

        # Fix last and first node's prev/next
        node.next = first
        first.prev = node

        # Return head node
        return first


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    # Initialize CLS, return head node for starting the traversal
    node = Node.make_list(num_people)

    # Loop until only 1 item left in lst (= survivor!)
    while node.next != node:

        # Land on node to remove
            # -1 bc we start on 1st node. If 3rd node, only jump 2x.
        for i in range(kill_every - 1):
            node = node.next

        # We've landed on node to remove. Remove.
        # Here, we essentially re-attach the prev and next nodes
            # together to rid of current node.
        node.prev.next = node.next
        node.next.prev = node.prev

        # Move to next node for next jump
        node = node.next

    # Return survivor's data
    return node.data


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
