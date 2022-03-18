import math
from dalpy.arrays import Array
from dalpy.stacks import Stack
from dalpy.queues import Queue
from dalpy.linked_lists import SinglyLinkedListNode, DoublyLinkedListNode

class BoundedDequeOverflowError(Exception):
    def __init__(self):
        super().__init__('BoundedDeque is full')


class BoundedDequeUnderflowError(Exception):
    def __init__(self):
        super().__init__('BoundedDeque is empty')


class NormalizedQueueUnderflowError(Exception):
    def __init__(self):
        super().__init__('NormalizedQueue is empty')


class TimedQueueUnderflowError(Exception):
    def __init__(self):
        super().__init__('TimedQueue is empty')


# ************************** DO NOT MODIFY ABOVE THIS LINE ******************************

class BoundedDeque:
    def __init__(self, capacity):
        pass

    def push_front(self, e):
        pass

    def pop_front(self):
        pass

    def push_back(self, e):
        pass

    def pop_back(self):
        pass


def intersect_queues(q1, q2):
    pass


def union_queues(q1, q2):
    pass


def difference_queues(q1, q2):
    pass


class NormalizedQueue:
    def __init__(self):
        pass

    def enqueue(self, e):
        pass

    def dequeue(self):
        pass

    def front(self):
        pass


class TimedQueue:
    def __init__(self):
        pass

    def enqueue(self, e):
        pass

    def dequeue(self):
        pass

    def front(self):
        pass
