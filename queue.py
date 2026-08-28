class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []

        curr = self.front
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        return "->".join(items)

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = self.rear = new_node
            self.size += 1

        else:
            self.rear.next = new_node
            self.rear = new_node
            self.size += 1

    def dequeue(self):
        if self.is_empty(): raise IndexError("Empty Queue!")

        dequeue_value = self.front.data
        self.front = self.front.next

        if self.is_empty(): self.rear = None

        self.size -= 1
        return dequeue_value

    def peek(self):
        if self.is_empty(): raise IndexError("Empty Queue!")
        return self.front.data

    def is_empty(self):
        return self.front is None and self.rear is None


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(11)
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)

    print(queue)
    print()
    print(len(queue))
    print()
    print(queue.peek())
    print()

    queue.dequeue()

    print(queue)
    print()
    print(queue.is_empty())