
class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def add(self, item):
        self.queue.append(item)

    # Remove an element
    def remove(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)

q.display()
#remove first element 
q.remove()

print("After removing an element")
q.display()