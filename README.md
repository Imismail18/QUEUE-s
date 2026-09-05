# Queue Data Structure

A simple Python implementation of a FIFO queue using a linked list.

## Overview

This project defines a `Queue` class that follows the First In, First Out (FIFO) principle:

- the first item added is the first item removed
- items are inserted at the rear
- items are removed from the front

The implementation uses internal `Node` objects and maintains `front`, `rear`, and `size` attributes.

## Files

- `queue.py` — contains the queue data structure and all related methods

## Features

- FIFO behavior
- efficient `enqueue` and `dequeue` operations in O(1)
- `peek()` to inspect the front element without removing it
- `len()` to get the current queue size
- `is_empty()` to check whether the queue is empty
- string output via `__repr__` showing the queue as `a->b->c`
- looping throgh the items via `__iter__`

## Queue Methods

- `enqueue(data)`: adds a value to the rear of the queue
- `dequeue()`: removes and returns the value at the front; raises `IndexError` if the queue is empty
- `peek()`: returns the front value without removing it; raises `IndexError` if the queue is empty
- `is_empty()`: returns `True` if the queue is empty, otherwise `False`
- `__len__()`: returns the current number of elements
- `__repr__()`: returns a readable representation of the queue
- `__iter__()`: inables looping the queue items

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
- `__len__`: O(1)
- `__repr__`: O(n)
- `__iter__`: O(n)

## Project Structure

```text
Stack/
├── queue.py
├── README.md
```

## Notes

- This queue is implemented with a singly linked list, not with Python's built-in list type.
- When the queue becomes empty after a dequeue, the `rear` pointer is reset to `None`.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## Author

Ismail - [@Imismail18](https://github.com/Imismail18)

## License

MIT License

Copyright (c) 2026 Ismail

This project is provided for educational purposes and can be used freely in personal or learning projects.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


