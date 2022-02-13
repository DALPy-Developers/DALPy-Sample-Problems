import math
import unittest

from cormen_lib.factory_utils import make_array
from cormen_lib.test_utils import build_and_run_watched_suite, behavior_test

from queue_problems import BoundedDeque, BoundedDequeOverflowError, BoundedDequeUnderflowError, \
    TimedQueue, \
    TimedQueueUnderflowError, NormalizedQueue, \
    NormalizedQueueUnderflowError


class BoundedDequeTest(unittest.TestCase):

    def test_back_operations(self):
        q = BoundedDeque(10)
        behavior = [(q.push_back, i) for i in range(5)] + [(i, q.pop_back) for i in range(4, -1, -1)] + [
            (q.push_back, i) for i in range(10)] + [(i, q.pop_back) for i in range(9, 4, -1)] + [
                       (q.push_back, i) for i in range(5)] + [(i, q.pop_back) for i in range(4, -1, -1)]
        behavior_test(behavior, q)

    def test_mixed_operations(self):
        q = BoundedDeque(10)
        behavior = [(q.push_back, i) for i in range(5)] + [(i, q.pop_front) for i in range(5)] + [
            (q.push_front, i) for i in range(10)] + [(i, q.pop_back) for i in range(5)] + [
                       (q.push_back, i) for i in range(5)] + [(i, q.pop_front) for i in range(9, 4, -1)]
        behavior_test(behavior, q)

    def test_front_operations(self):
        q = BoundedDeque(10)
        behavior = [(q.push_front, i) for i in range(5)] + [(i, q.pop_front) for i in range(4, -1, -1)] + [
            (q.push_front, i) for i in range(10)] + [(i, q.pop_front) for i in range(9, 4, -1)] + [
                       (q.push_front, i) for i in range(5)] + [(i, q.pop_front) for i in range(4, -1, -1)]
        behavior_test(behavior, q)

    def test_overflow_front_push(self):
        q = BoundedDeque(5)
        behavior = [(q.push_front, i) for i in range(5)] + [(BoundedDequeOverflowError, q.push_front, 5)]
        behavior_test(behavior, q)

    def test_overflow_back_push(self):
        q = BoundedDeque(5)
        behavior = [(q.push_back, i) for i in range(5)] + [(BoundedDequeOverflowError, q.push_back, 5)]
        behavior_test(behavior, q)

    def test_overflow_mixed_push(self):
        q = BoundedDeque(5)
        behavior = [(q.push_front, i) if i % 2 == 0 else (q.push_back, i) for i in range(5)] + [
            (BoundedDequeOverflowError, q.push_back, 5)]
        behavior_test(behavior, q)
        q = BoundedDeque(5)
        behavior = [(q.push_back, i) if i % 2 == 0 else (q.push_front, i) for i in range(5)] + [
            (BoundedDequeOverflowError, q.push_front, 5)]
        behavior_test(behavior, q)

    def test_overflow_after_pop_mixed(self):
        q = BoundedDeque(5)
        behavior = [(q.push_front, 0) if i % 2 == 1 else (q.push_back, 0) for i in range(5)] + [
            (0, q.pop_back) if i % 2 == 1 else (0, q.pop_front) for i in range(3)] + [
                       (q.push_front, 0) if i % 2 == 0 else (q.push_back, 0) for i in range(3)] + [
                       (BoundedDequeOverflowError, q.push_back, 5)]
        behavior_test(behavior, q)

    def test_underflow_front_pop(self):
        q = BoundedDeque(100)
        behavior = [(q.push_front, 0), (0, q.pop_front), (BoundedDequeUnderflowError, q.pop_front)]
        behavior_test(behavior, q)

    def test_underflow_back_push(self):
        q = BoundedDeque(100)
        behavior = [(q.push_back, 0), (0, q.pop_back), (BoundedDequeUnderflowError, q.pop_back)]
        behavior_test(behavior, q)

    def test_push_front_then_pop_back(self):
        q = BoundedDeque(100)
        behavior = [(q.push_front, 0), (0, q.pop_back)]
        behavior_test(behavior, q)

    def test_push_back_then_pop_front(self):
        q = BoundedDeque(100)
        behavior = [(q.push_back, 0), (0, q.pop_front)]
        behavior_test(behavior, q)


class NormalizedQueueTest(unittest.TestCase):

    def test_single_dequeue(self):
        q = NormalizedQueue()
        behavior = [
            (q.enqueue, 1),
            (1, q.dequeue),
            (q.enqueue, 2),
            (1, q.dequeue)
        ]
        behavior_test(behavior, q)

    def test_simple_behavior(self):
        q = NormalizedQueue()
        behavior = [(q.enqueue, i) for i in range(1, 4)] + [(x, q.dequeue) for x in
                                                            [1 / math.sqrt(14), 2 / math.sqrt(13), 3 / math.sqrt(9)]]
        behavior_test(behavior, q)

    def test_advanced_behavior(self):
        q = NormalizedQueue()
        behavior = [
                       (q.enqueue, 2),
                       (q.enqueue, 2),
                       (2 / math.sqrt(8), q.dequeue),
                       (q.enqueue, 1),
                       (q.enqueue, 4),
                   ] + [(x, q.dequeue) for x in [2 / math.sqrt(21), 1 / math.sqrt(17), 4 / math.sqrt(16)]]
        behavior_test(behavior, q)

    def test_simple_behavior_with_front(self):
        q = NormalizedQueue()
        behavior = [(q.enqueue, i) for i in range(1, 4)] + [
            (1 / math.sqrt(14), q.front),
            (1 / math.sqrt(14), q.dequeue),
            (2 / math.sqrt(13), q.front),
            (2 / math.sqrt(13), q.dequeue),
            (3 / math.sqrt(9), q.front),
            (3 / math.sqrt(9), q.dequeue)
        ]
        behavior_test(behavior, q)

    def test_negative_numbers(self):
        q = NormalizedQueue()
        behavior = [(q.enqueue, -1 * i if i % 2 == 1 else i) for i in range(1, 4)] + [
            (-1 / math.sqrt(14), q.front),
            (-1 / math.sqrt(14), q.dequeue),
            (2 / math.sqrt(13), q.front),
            (2 / math.sqrt(13), q.dequeue),
            (-3 / math.sqrt(9), q.front),
            (-3 / math.sqrt(9), q.dequeue)
        ]
        behavior_test(behavior, q)

    def test_zero(self):
        q = NormalizedQueue()
        behavior = [(q.enqueue, i) for i in range(3)] + [(x, q.dequeue) for x in
                                                         [0, 1 / math.sqrt(5), 2 / math.sqrt(4)]]
        behavior_test(behavior, q)

    def test_underflow(self):
        q = NormalizedQueue()
        behavior = [
            (q.enqueue, 1),
            (1, q.dequeue),
            (NormalizedQueueUnderflowError, q.dequeue)
        ]
        behavior_test(behavior, q)


class TimedQueueTest(unittest.TestCase):

    def test_pdf_behavior(self):
        q = TimedQueue()
        behavior = [(q.enqueue, x) for x in ['a', 'b', 'c']] + [
            (make_array(['a', 2]), q.dequeue),
            (make_array(['b', 2]), q.dequeue),
            (make_array(['c', 2]), q.front),
            (make_array(['c', 3]), q.dequeue)
        ]
        behavior_test(behavior, q)

    def test_single_dequeue(self):
        q = TimedQueue()
        behavior = [
            (q.enqueue, 'a'),
            (make_array(['a', 0]), q.dequeue),
            (q.enqueue, 'b'),
            (make_array(['b', 0]), q.dequeue)
        ]
        behavior_test(behavior, q)

    def test_advanced_behavior(self):
        q = TimedQueue()
        behavior = [
                       (q.enqueue, 'a'),
                       (q.enqueue, 'b'),
                       (make_array(['a', 1]), q.dequeue),
                       (q.enqueue, 'c'),
                       (q.enqueue, 'd'),
                       (q.enqueue, 'e'),
                       (make_array(['b', 4]), q.front),
                       (make_array(['b', 5]), q.dequeue)
                   ] + [(make_array([x, 4]), q.dequeue) for x in ['c', 'd', 'e']]
        behavior_test(behavior, q)

    def test_multiple_front(self):
        q = TimedQueue()
        behavior = [(q.enqueue, 'a')] + [(make_array(['a', i]), q.front) for i in range(4)] + [
            (make_array(['a', 4]), q.dequeue)]
        behavior_test(behavior, q)

    def test_underflow(self):
        q = TimedQueue()
        behavior = [
            (q.enqueue, 0),
            (make_array([0, 0]), q.dequeue),
            (TimedQueueUnderflowError, q.dequeue)
        ]
        behavior_test(behavior, q)


if __name__ == '__main__':
    build_and_run_watched_suite(
        [BoundedDequeTest, NormalizedQueueTest, TimedQueueTest], timeout=4)
