# Queue Data Structure

A simple Python implementation of a FIFO queue using a linked list.

## Overview

This project defines a `Queue` class that follows the First In, First Out (FIFO) principle:

- The first element added is the first one removed.
- Elements are added at the rear.
- Elements are removed from the front.

The implementation includes common queue operations such as `enqueue`, `dequeue`, `peek`, `is_empty`, and `len`.

## Files

- `queue.py` — contains the queue implementation.

## Features

- FIFO behavior
- Constant-time enqueue and dequeue operations
- `peek()` to view the front element without removing it
- `len()` to get the current queue size
- `is_empty()` to check whether the queue is empty

## Example

```python
from queue import Queue

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(len(q))      # 3
print(q.peek())    # 10
print(q)           # 10->20->30

q.dequeue()
print(q)           # 20->30
```

## Time Complexity

- `enqueue`: O(1)
- `dequeue`: O(1)
- `peek`: O(1)
- `is_empty`: O(1)
- `__repr__`: O(n)

## License

This project is provided for educational purposes and can be used freely in personal or learning projects.
