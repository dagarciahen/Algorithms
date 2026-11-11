"""
Merge Overlapping Intervals
Medium

Merge an array of intervals so there are no overlapping intervals, and return
the resultant merged intervals.

Example:
Input: intervals = [[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]]
Output: [[1, 5], [6, 8]]

Constraints:
The input contains at least one interval.
"""


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def merge_overlapping_intervals(intervals):
    raise NotImplementedError()


def to_intervals(pairs):
    return [Interval(s, e) for s, e in pairs]


def to_pairs(intervals):
    return [[i.start, i.end] for i in intervals]


def run_test(intervals, expected, test_name):
    print(test_name)
    print("intervals = " + str(intervals))
    print("expected  = " + str(expected))

    try:
        actual = to_pairs(merge_overlapping_intervals(to_intervals(intervals)))
        print("actual    = " + str(actual))
        print("pass      = " + str(actual == expected))
    except NotImplementedError:
        print("actual    = not implemented")

    print()


if __name__ == "__main__":
    run_test([[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]], [[1, 5], [6, 8]], "Test 1")
    run_test([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]], "Test 2")
    run_test([[1, 4], [4, 5]], [[1, 5]], "Test 3")
    run_test([[1, 4], [2, 3]], [[1, 4]], "Test 4")
    run_test([[5, 7], [1, 2], [2, 3]], [[1, 3], [5, 7]], "Test 5")
