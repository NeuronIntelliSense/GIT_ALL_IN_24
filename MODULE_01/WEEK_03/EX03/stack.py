class Stack:
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

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.list_element.pop()

    def push(self, element):
        if self.is_full():
            print("Stack is full")
        else:
            self.list_element.append(element)

    def top(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.list_element[-1]
