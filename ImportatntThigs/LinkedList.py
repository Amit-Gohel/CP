class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        
        itr = self.head
        print(str(itr.data), end='')
        itr = itr.next
        while itr:
            print(' --> ' + str(itr.data), end = '')
            itr = itr.next
        print()

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            return Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            return Exception("Invaild Index")
        
        if index == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.printList()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.printList()