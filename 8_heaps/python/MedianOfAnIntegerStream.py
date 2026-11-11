"""
Median of an Integer Stream
Hard

Design a data structure that supports adding integers from a data stream and
retrieving the median of all elements received at any point.

add(num: int) -> None: adds an integer to the data structure.
get_median() -> float: returns the median of all integers so far.

Example:
Input: [add(3), add(6), get_median(), add(1), get_median()]
Output: [4.5, 3.0]

Explanation:
add(3)        # data structure contains [3] when sorted
add(6)        # data structure contains [3, 6] when sorted
get_median()  # median is (3 + 6) / 2 = 4.5
add(1)        # data structure contains [1, 3, 6] when sorted
get_median()  # median is 3.0
"""


class MedianOfAnIntegerStream:
    def __init__(self):
        pass

    def add(self, num: int) -> None:
        raise NotImplementedError()

    def get_median(self) -> float:
        raise NotImplementedError()


def run_test(ops, expected, test_name):
    print(test_name)
    print("ops      = " + str(ops))
    print("expected = " + str(expected))

    try:
        stream = MedianOfAnIntegerStream()
        actual = []
        for op in ops:
            if op[0] == "add":
                stream.add(op[1])
            elif op[0] == "get_median":
                actual.append(stream.get_median())
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([("add", 3), ("add", 6), ("get_median",), ("add", 1), ("get_median",)], [4.5, 3.0], "Test 1")
    run_test([("add", 5), ("get_median",)], [5.0], "Test 2")
    run_test([("add", -1), ("add", -2), ("add", -3), ("get_median",)], [-2.0], "Test 3")
    run_test([("add", 2), ("add", 2), ("add", 2), ("get_median",), ("add", 4), ("get_median",)], [2.0, 2.0], "Test 4")
    run_test([("add", 1), ("add", 2), ("add", 3), ("add", 4), ("add", 5), ("get_median",)], [3.0], "Test 5")
