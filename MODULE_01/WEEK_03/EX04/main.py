from queue import Queue

if __name__ == "__main__":
    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)

    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())
