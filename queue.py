"""
Structure of comments:
Function description.
Time complexity O()
"""

#Queue Node class - Represents a single node in the Queue data structure.
class Node:
    #Initializes the node with data and a reference to the next node.
    #Time complexity: O(1)
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Queue class - Implements a queue data structure using a linked list.
#FIFO (First In First Out) principle: elements are added at rear and removed from front.
class Queue:
    #Initializes an empty queue with front and rear pointers set to None and size counter set to 0.
    #Time complexity: O(1)
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    #Returns the number of elements currently in the queue.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #loops throgh the queue items and return the items to be iterited later if needed. note that the items are in string format.
    #Time complexity: O(n)
    #Queue Node class - Represents a single node in the Queue data structure.
class Node:
    #Initializes the node with data and a reference to the next node.
    #Time complexity: O(1)
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Queue class - Implements a queue data structure using a linked list.
#FIFO (First In First Out) principle: elements are added at rear and removed from front.
class Queue:
    #Initializes an empty queue with front and rear pointers set to None and size counter set to 0.
    #Time complexity: O(1)
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    #Returns the number of elements currently in the queue.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #Loops the queue's items and return those items to be used in iteriitions.
    #Time complexity: O(n)
    def __iter__(self):
        items = []

        curr = self.front
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        yield from items

    #Returns a string representation of the queue showing all elements from front to rear.
    #Time complexity: O(n), where n is the number of elements in the queue.
    def __repr__(self):
        if self.is_empty(): return "[]"

        items = []

        curr = self.front
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")

        return "->".join(items)

    #Adds an element to the rear of the queue.
    #Time complexity: O(1)
    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty(): self.front = self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    #Removes and returns the element at the front of the queue. Raises IndexError if queue is empty.
    #Time complexity: O(1)
    def dequeue(self):
        if self.is_empty(): raise IndexError("Empty Queue!")

        dequeue_value = self.front.data
        self.front = self.front.next

        if self.is_empty(): self.rear = None

        self.size -= 1

        return dequeue_value

    #Returns the element at the front of the queue without removing it. Raises IndexError if queue is empty.
    #Time complexity: O(1)
    def peek(self):
        if self.is_empty(): raise IndexError("Empty Queue!")
        return self.front.data

    #Checks if the queue is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.front is None and self.rear is None


    #Returns a string representation of the queue showing all elements from front to rear.
    #Time complexity: O(n), where n is the number of elements in the queue.
    def __repr__(self):
        if self.is_empty(): return "[]"
            
        items = []

        curr = self.front
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")
        
        return "->".join(items)

    #Adds an element to the rear of the queue.
    #Time complexity: O(1)
    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty(): self.front = self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    #Removes and returns the element at the front of the queue. Raises IndexError if queue is empty.
    #Time complexity: O(1)
    def dequeue(self):
        if self.is_empty(): raise IndexError("Empty Queue!")

        dequeue_value = self.front.data
        self.front = self.front.next

        if self.is_empty(): self.rear = None

        self.size -= 1
        
        return dequeue_value

    #Returns the element at the front of the queue without removing it. Raises IndexError if queue is empty.
    #Time complexity: O(1)
    def peek(self):
        if self.is_empty(): raise IndexError("Empty Queue!")
            
        return self.front.data

    #Checks if the queue is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.front is None and self.rear is None


if __name__ == "__main__":
    print("==" * 30, "\nQueue data structure:\nBeginning:\n", "__" * 30)
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(11)
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)

    print()
    print(queue)
    print(len(queue))
    print(queue.peek())

    queue.dequeue()

    print(queue)
    print(queue.is_empty())

    for i in queue: print(i)
        
    print("==" * 30, "\nQueue data structure - End\n")
