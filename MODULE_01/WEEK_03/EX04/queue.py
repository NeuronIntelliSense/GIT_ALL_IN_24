class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list_element = []

    def is_empty(self):
        if len(self.list_element) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.list_element) == self.capacity:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.list_element.pop(0)

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full")
        else:
            self.list_element.append(element)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.list_element[0]
