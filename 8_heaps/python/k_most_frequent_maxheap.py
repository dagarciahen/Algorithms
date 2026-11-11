
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
from collections import Counter
from typing import List

class Entry:
    def __init__(self, item, frequency):
        self.item = item
        self.frequency = frequency

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.item < other.item
        return self.frequency > other.frequency
    
    def __repr__(self):
        return f"({self.item},{self.frequency})"
    
    

class MaxHeap:
    def __init__(self):
        self.entries= []
        
    def append(self, item, frequency):
        self.entries.append(Entry(item, frequency))
        self.upheap(len(self.entries)-1)

    def swap(self, a, b):
        L = self.entries
        L[a], L[b] = L[b], L[a]
        
    def upheap(self, i):
        L = self.entries
        parent = (i-1)//2
        if i > 0 and L[i] < L[parent]:
            self.swap(i, parent)
            self.upheap(parent)
    
    def removemax(self):
        L = self.entries
        item = L[0].item
        self.swap(0, -1)
        L.pop()
        self.downheap(0)
        return item

    def downheap(self, i):
        L = self.entries
        left = 2*i+1
        right = 2*i+2
        child = left
        children = range(left, min(right+1, len(self.entries)))
        if children:
            #child = max(children, key = lambda x : L[x])
            for j in children:
                if L[j] < L[child]:
                    child = j
            if L[child] < L[i]:
                self.swap(child, i)
                self.downheap(child)


def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    maxheap = MaxHeap()
    freqs = Counter(strs)
    for word, freq in freqs.items():
        maxheap.append(word, freq)
    res = []
    for _ in range(k):
        maxheap.entries
        res.append(maxheap.removemax())

    return res

"""
complexity analysis:
creating the maxheap will take O(nlogn) because upheap will take at most logn as the index is dived by half, 
then by n elements
then removemax is O(logn) k times O(klogn) 
the complexity is O(nlogn) + O(klogn) = O((n+k)logn) -> O(nlogn) pbecause k <= n

space complexity is the O(n) of the hashmap to count elements

"""






##in maxheap I want to move up the most frequent elements if two elements have the same frequency i have to order them by lexicographical order
##this means I want the less alpha order element to leave the heap first a then b 

def run_test(strs, k, expected, test_name):
    print(test_name)
    print("strs     = " + str(strs))
    print("k        = " + str(k))
    print("expected = " + str(expected))

    try:
        actual = k_most_frequent_strings(strs, k)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test(['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go'], 2, ['go', 'byte'], "Test 1")
    run_test(['a', 'b', 'a'], 1, ['a'], "Test 2")
    run_test(['x', 'y', 'z'], 3, ['x', 'y', 'z'], "Test 3")
    run_test(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2, ['i', 'love'], "Test 4")
    run_test(['aaa', 'aa', 'a', 'aaa', 'aa', 'a'], 1, ['a'], "Test 5")
