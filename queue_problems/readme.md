# Queue Problems

## Bounded Deque
A deque is a data structure that supports the following operations:
- ```push_front(x)```: insert item x on the front end of the deque.
- ```pop_front()```: remove the front item from the deque and return it.
- ```push_back(x)```: insert item x on the rear end of the deque.
- ```pop_back()```: remove the rear item from the deque and return it.

Create a data structure ```BoundedDeque``` that supports the deque operations in O(1) time. ```BoundedDeque``` has a fixed capacity n. 

In the event where an attempt is made to insert an n+1th element into the ```BoundedDeque``` it should raise a ```BoundedDequeueOverflowError```. Similarly, if the user attempts to remove an element from the ```BoundedDeque``` when it is empty, it should raise a ```BoundedDequeUnderflowError```.
You cannot use ```DoublyLinkedListNode``` for this problem.

## Normalized Queue

Create a data structure ```NormalizedQueue``` that is an unbounded queue data structure where every read or removed element is normalized. The queue operations that ```NormalizedQueue``` must support are ```enqueue```, ```dequeue```, and ```front```. Each operation must run in O(1) time. 

A ```NormalizedQueue q``` should work as follows:
```
q = NormalizedQueue()
q.enqueue(1)
q.enqueue(-2)
q.enqueue(3)
x = q.dequeue()
y = q.front()
```
Instead of ```x``` storing ```1```, it should store ```1``` normalized with respect to the elements in the queue prior to its removal. That is, ```x``` should be: 1/sqrt(1^2 + (-2)^2 + 3^2) ≈ 0.267261. Similarly, ```y``` should store ```-2``` normalized with respect to the elements in the queue: -2/sqrt((-2)^2 + 3^2)≈ −0.554700.

You may assume that all elements that are enqueued are positive or negative real numbers.

## Timed Queue
Create a data structure ```TimedQueue``` that is an unbounded queue data structure which tracks the time each element spent in the data structure. The queue operations that ```TimedQueue``` must support are ```enqueue```, ```dequeue```, and ```front```. Each operation must run in O(1) time. The time an element ```e``` spends in the data structure is the number of operations that were performed since ```e``` was enqueued. 

As an example, consider the following table. The colums a, b, and c represent the time that element has spent in the queue by the current operation.

Operation | a | b | c | Return
--- | --- | --- | --- | ---
```enqueue(a)``` | 1 |  |  |
```enqueue(b)``` | 2 | 1 |  | 
```enqueue(c)``` | 3 | 2 | 1 | 
```dequeue()``` |  | 3 | 2 | ```(a,3)```
```dequeue()``` |  |  | 3 | ```(b,3)```
```front()``` |  |  | 4 | ```(c,3)```
```dequeue()``` |  |  |  | ```(c,4)```
