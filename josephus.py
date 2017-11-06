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


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
