"""
Identify All Interval Overlaps
Medium

Return an array of all overlaps between two arrays of intervals; intervals1 and
intervals2. Each individual interval array is sorted by start value, and contains
no overlapping intervals within itself.

Example:
Input: intervals1 = [[1, 4], [5, 6], [9, 10]],
       intervals2 = [[2, 7], [8, 9]]
Output: [[2, 4], [5, 6], [9, 9]]

Constraints:
For every index i in intervals1, intervals1[i].start < intervals1[i].end.
"""


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def identify_all_interval_overlaps(intervals1, intervals2):
    raise NotImplementedError()


def to_intervals(pairs):
    return [Interval(s, e) for s, e in pairs]


def to_pairs(intervals):
    return [[i.start, i.end] for i in intervals]


def run_test(intervals1, intervals2, expected, test_name):
    print(test_name)
    print("intervals1 = " + str(intervals1))
    print("intervals2 = " + str(intervals2))
    print("expected   = " + str(expected))

    try:
        actual = to_pairs(identify_all_interval_overlaps(to_intervals(intervals1), to_intervals(intervals2)))
        print("actual     = " + str(actual))
        print("pass       = " + str(actual == expected))
    except NotImplementedError:
        print("actual     = not implemented")

    print()


if __name__ == "__main__":
    run_test([[1, 4], [5, 6], [9, 10]], [[2, 7], [8, 9]], [[2, 4], [5, 6], [9, 9]], "Test 1")
    run_test([[1, 5]], [[6, 8]], [], "Test 2")
    run_test([[1, 5], [10, 12]], [[3, 8], [9, 11]], [[3, 5], [10, 11]], "Test 3")
    run_test([[0, 2]], [[0, 2]], [[0, 2]], "Test 4")
    run_test([[1, 4], [7, 8]], [[2, 3], [5, 6]], [[2, 3]], "Test 5")
