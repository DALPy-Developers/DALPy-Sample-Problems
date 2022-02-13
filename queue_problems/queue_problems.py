import math
from cormen_lib.arrays import Array
from cormen_lib.stacks import Stack
from cormen_lib.queues import Queue
from cormen_lib.linked_lists import SinglyLinkedListNode, DoublyLinkedListNode


# ************************** DO NOT MODIFY ABOVE THIS LINE ******************************


class BoundedDequeOverflowError(Exception):
    def __init__(self):
        super().__init__('BoundedDeque is full')


class BoundedDequeUnderflowError(Exception):
    def __init__(self):
        super().__init__('BoundedDeque is empty')


class BoundedDeque:
    def __init__(self, capacity):
        self.buf = Array(capacity)
        self.head = 0
        self.tail = 0
        self.num_entries = 0

    def __check_full(self):
        if self.num_entries == self.buf.length():
            raise BoundedDequeOverflowError()

    def __check_empty(self):
        if self.num_entries == 0:
            raise BoundedDequeUnderflowError()

    def __reset_tail(self):
        if self.num_entries == 1:
            self.tail = self.head

    def __reset_head(self):
        if self.num_entries == 1:
            self.head = self.tail

    def push_front(self, e):
        self.__check_full()
        self.head = self.buf.length() - 1 if self.head == 0 else self.head - 1
        self.buf[self.head] = e
        self.num_entries += 1
        self.__reset_tail()

    def pop_front(self):
        self.__check_empty()
        out = self.buf[self.head]
        self.head = (self.head + 1) % self.buf.length()
        self.num_entries -= 1
        return out

    def push_back(self, e):
        self.__check_full()
        self.tail = (self.tail + 1) % self.buf.length()
        self.buf[self.tail] = e
        self.num_entries += 1
        self.__reset_head()

    def pop_back(self):
        self.__check_empty()
        out = self.buf[self.tail]
        self.tail = self.buf.length() - 1 if self.num_entries == 1 else self.tail - 1
        self.num_entries -= 1
        return out

    def front(self):
        self.__check_empty()
        return self.buf[self.head]

    def back(self):
        self.__check_empty()
        return self.buf[self.tail]

    def size(self):
        return self.num_entries

    def is_empty(self):
        return self.num_entries == 0


class NormalizedQueueUnderflowError(Exception):
    def __init__(self):
        super().__init__('NormalizedQueue is empty')
        
# Treat it like vector normalization
class NormalizedQueue:
    def __init__(self):
        self.sum_of_squares = 0
        self.queue = Queue()

    def __check_empty(self):
        if self.queue.is_empty():
            raise NormalizedQueueUnderflowError()

    def enqueue(self, e):
        self.sum_of_squares += e**2
        self.queue.enqueue(e)

    def dequeue(self):
        self.__check_empty()
        removed = self.queue.dequeue()
        out = removed / math.sqrt(self.sum_of_squares)
        self.sum_of_squares -= removed**2
        return out

    def front(self):
        self.__check_empty()
        first = self.queue.front()
        return (first / math.sqrt(self.sum_of_squares)) if self.sum_of_squares > 0 else first

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()


class TimedQueueUnderflowError(Exception):
    def __init__(self):
        super().__init__('TimedQueue is empty')


class TimedQueue:
    def __init__(self):
        self.num_ops = 0
        self.data = Queue()
        self.entry_times = Queue()

    def enqueue(self, e):
        self.num_ops += 1
        self.data.enqueue(e)
        self.entry_times.enqueue(self.num_ops)

    def __check_empty(self):
        if self.data.is_empty():
            raise TimedQueueUnderflowError()

    def dequeue(self):
        self.__check_empty()
        out = Array(2)
        out[0] = self.data.dequeue()
        out[1] = self.num_ops - self.entry_times.dequeue()
        self.num_ops += 1
        return out

    def front(self):
        self.__check_empty()
        out = Array(2)
        out[0] = self.data.front()
        out[1] = self.num_ops - self.entry_times.front()
        self.num_ops += 1
        return out

    def size(self):
        return self.data.size()

    def is_empty(self):
        return self.data.is_empty()
