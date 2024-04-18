#!/usr/bin/python3
''' lockboxes module '''
from collections import deque
"""
--------------------- explanation ---------------------
- we have n boxes and and each box has a list of keys to other boxes
- we can always open the first box which mean we have the key to box 0
    (keys = {0})
- we need to check if we can open all the boxes
- we can use a queue(deque) to keep track of the boxes we can open
- we start by adding the first box to the queue
- we continue by popping the first box from the queue and
  adding the keys to the keys set
- we also add the keys to the queue if they are not already in the keys
  set so that next
- when we pop left the queue we can check the keys of the next box
- then we loop until the queue is empty

- Important: order matters, we can only open the boxes we have key for
  to ensure that we can open all boxes

- Time complexity: O(n) where n is the number of boxes
"""


def canUnlockAll(boxes):
    """ can unlock all boxes """
    keys = set([0])
    queue = deque([0])

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key not in keys and key < len(boxes):
                keys.add(key)
                queue.append(key)

    return len(keys) == len(boxes)
