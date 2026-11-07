"""
K Most Frequent Strings
Medium
Find the k most frequently occurring strings in an array, and return them sorted by frequency in descending order. If two strings have the same frequency, sort them in lexicographical order.

Input: strs = ['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go'], k = 2
Output: ['go', 'byte']

Explanation: The strings "go" and "byte" appear the most frequently, with frequencies of 3 and 2, respectively.

Constraints:
k ≤ n, where n denotes the length of the array.

"""
from typing import List
import heapq
from Collections import Entry

class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.item > other.priority
        return self.priority < other.priority



def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    freqs = Counter(srs)
    min_heap = []
    for word in strs.items():
        heapq.heappush(min_heap, word.item)
        #only the most frequen k strings remain
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    res = []
    for _ in range(k):
        res.append(heapq.heappop(min_heap).item)
    res.reverse()
    return res










def test(strs, expected):
    result = k_most_frequent(strs)

    print(f"strs:   {strs}")
    print(f"expected: {output}")
    print(f"result:   {result}")

    assert result == expected
    print("PASS")

test(strs, output)
