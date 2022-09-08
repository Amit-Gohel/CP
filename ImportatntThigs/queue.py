class Queue:
    def __init__(self):
        self.s = []


    def enqueue(self, data):
        return self.s.insert(0, data)


    def peek(self):
        if not self.is_empty():
            return self.s[-1]
        return "List is empty"


    def dequeue(self):
        if not self.is_empty():
            return self.s.pop()
        print("List is empty")


    def is_empty(self):
        return len(self.s) == 0


    def size_of(self):
        return len(self.s)


q = Queue()
q.enqueue(3)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(2)
q.dequeue()
print(q.peek())