import heapq
import itertools
from dataclasses import dataclass, field
from typing import Any


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
heapq.heappush(h)

"""A priority queue is common use for a heap, and it presents several
    implementation challenges:

Sort stability: how do you get two tasks with equal priorities to be 
    returned in the order they were originally added?

Tuple comparison breaks for (priority, task) pairs if the priorities
    are equal and the tasks do not have a default comparison order.

If the priority of a task changes, how do you move it to a new position
    in the heap?

Or if a pending task needs to be deleted, how do you find it and remove
    it from the queue?"""

'''

A solution to the first two challenges is to store entries as 3-element
list including the priority, an entry count, and the task.
 
The entry count serves as a tie-breaker so that two tasks with the same
priority are returned in the order they were added. And since no two entry
counts are the same, the tuple comparison will never attempt to directly
compare two task

Another solution to the problem of non-comparable tasks is to
create a wrapper class to ignore task item and only compare the priority field

'''


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = '<removed-task>'  # placeholder for a removed task
counter = itertools.count()  # unique sequence count


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)


def remove_task(task):
    """Mark an existing task as REMOVED.  Raise KeyError if not found."""
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    """Remove and return the lowest priority task. Raise KeyError if empty."""
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')
