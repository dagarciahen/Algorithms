"""
Largest Overlap of Intervals
Medium

Given an array of intervals, determine the maximum number of intervals that
overlap at any point. Each interval is half-open, meaning it includes the start
point but excludes the end point.

Example:
Input: intervals = [[1, 3], [5, 7], [2, 6], [4, 8]]
Output: 3

Constraints:
The input will contain at least one interval.
For every index i in the list, intervals[i].start < intervals[i].end.
"""


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def largest_overlap_of_intervals(intervals):
    raise NotImplementedError()


def to_intervals(pairs):
    return [Interval(s, e) for s, e in pairs]


def run_test(intervals, expected, test_name):
    print(test_name)
    print("intervals = " + str(intervals))
    print("expected  = " + str(expected))

    try:
        actual = largest_overlap_of_intervals(to_intervals(intervals))
        print("actual    = " + str(actual))
        print("pass      = " + str(actual == expected))
    except NotImplementedError:
        print("actual    = not implemented")

    print()


if __name__ == "__main__":
    run_test([[1, 3], [5, 7], [2, 6], [4, 8]], 3, "Test 1")
    run_test([[1, 2], [2, 3], [3, 4]], 1, "Test 2")
    run_test([[1, 4], [2, 3], [3, 5]], 2, "Test 3")
    run_test([[1, 10], [2, 3], [4, 5], [6, 7]], 2, "Test 4")
    run_test([[1, 2], [1, 2], [1, 2]], 3, "Test 5")
