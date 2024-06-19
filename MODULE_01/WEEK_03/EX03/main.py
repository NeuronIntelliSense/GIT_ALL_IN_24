from stack import Stack

if __name__ == "__main__":
    stack1 = Stack(capacity=5)
    stack1.push(1)
    stack1.push(2)

    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())
