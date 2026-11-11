"""
Implement a Queue using Stacks

Medium

Implement a queue using the stack data structure. Include the following functions:

enqueue(x: int) -> None: adds x to the end of the queue.

dequeue() -> int: removes and returns the element from the front of the queue.

peek() -> int: returns the front element of the queue.

You may not use any other data structures to implement the queue.

Example:
Input: [enqueue(1), enqueue(2), dequeue(), enqueue(3), peek()]
Output: [1, 2]


"""

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, x) -> None:
        self.enqueue_stack.append(x)

    def transfer_enqueue_to_dequeue(self) -> None:
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

    def dequeue(self) -> None:
        self.transfer_enqueue_to_dequeue()
        return self.dequeue_stack.pop() if self.dequeue_stack else None 


    def peek(self) -> int:
        self.transfer_enqueue_to_dequeue()
        return self.dequeue_stack[-1] if self.dequeue_stack else None

def run_tests():
    tests = [
        {
            "name": "Single enqueue",
            "ops": [("enqueue", 10)],
            "expected_peek": 10,
        },
        {
            "name": "Basic FIFO order",
            "ops": [("enqueue", 1), ("enqueue", 2)],
            "expected_dequeue": 1,
        },
        {
            "name": "Multiple elements",
            "ops": [("enqueue", 5), ("enqueue", 6), ("enqueue", 7)],
            "expected_dequeue": 5,
        },
        {
            "name": "Peek does not remove element",
            "ops": [("enqueue", 100), ("enqueue", 200)],
            "expected_peek": 100,
            "expected_dequeue": 100,
        },
        {
            "name": "Complete FIFO sequence",
            "ops": [("enqueue", 1), ("enqueue", 2), ("enqueue", 3)],
            "expected_sequence": [1, 2, 3],
        },
    ]

    for i, test in enumerate(tests, start=1):
        q = Queue()

        for operation in test["ops"]:
            q.enqueue(operation[1])

        try:
            if "expected_peek" in test:
                assert q.peek() == test["expected_peek"]

            if "expected_dequeue" in test:
                assert q.dequeue() == test["expected_dequeue"]

            if "expected_sequence" in test:
                result = [q.dequeue() for _ in test["expected_sequence"]]
                assert result == test["expected_sequence"]

            print(f"✅ Test {i}: {test['name']}")

        except AssertionError:
            print(f"❌ Test {i}: {test['name']}")


if __name__ == "__main__":
    run_tests()
