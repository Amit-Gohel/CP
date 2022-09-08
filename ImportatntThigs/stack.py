class Stack:
    def __init__(self):
        self.s = []

    
    def push(self, data):
        return self.s.append(data)
    

    def peek(self):
        if not self.is_empty():
            return self.s[-1]
        return "List is empty"
    

    def pop(self):
        if not self.is_empty():
            return self.s.pop()
        print("List is empty")
        
    
    def is_empty(self):
        return len(self.s) == 0


    def size_of(self):
        return len(self.s)



s = Stack()
s.push(1)
s.push(2)
s.push(5)
print(s.size_of())
print(s.peek())
s.pop()
print(s.peek())
print(s.is_empty())
s.pop()
s.pop()
print(s.peek())
s.pop()
print(s.size_of())
print(s.is_empty())