"""
Find the Median From Two Sorted Arrays

Given two sorted integer arrays, find their median value as if they were
merged into a single sorted sequence.

Example 1:
Input: nums1 = [0, 2, 5, 6, 8], nums2 = [1, 3, 7]
Output: 4.0

Example 2:
Input: nums1 = [0, 2, 5, 6, 8], nums2 = [1, 3, 7, 9]
Output: 5.0

Constraints:
At least one of the input arrays will contain an element.
"""


def find_median_sorted_arrays(nums1, nums2):



def run_test(nums1, nums2, expected, test_name):
    print(test_name)
    print("nums1    = " + str(nums1))
    print("nums2    = " + str(nums2))
    print("expected = " + str(expected))

    try:
        actual = find_median_sorted_arrays(nums1, nums2)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([0, 2, 5, 6, 8], [1, 3, 7], 4.0, "Test 1")
    run_test([0, 2, 5, 6, 8], [1, 3, 7, 9], 5.0, "Test 2")
    run_test([1, 2], [3, 4], 2.5, "Test 3")
    run_test([], [7], 7.0, "Test 4")
    run_test([2], [], 2.0, "Test 5")



"""
def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums2, nums1 = nums1, nums2
    m = len(nums1)
    n = len(nums2)
    half_total_len = (m+n)//2
    left, right = 0, m-1
    while True:
        L1_index = left + (right-left)//2
        #sizeleftpartition = L1_index +1  
        #half_total_len = L1_index +1 + L2_index+1
        L2_index = half_total_len - L1_index - 2
        
        L1 = float('-inf') if L1_index < 0 else nums1[L1_index]
        R1 = float('inf') if L1_index >= m -1 else nums1[L1_index+1]
        L2 = float('-inf') if L2_index < 0 else nums2[L2_index]
        R2 = float('inf') if L2_index >= n-1 else nums2[L2_index+1]

        if L1 > R2:
            right = L1_index -1
        elif L2 > R1:
            left = L1_index +1 
        else:
            if (m+n)%2 == 0:
                return (max(L1,L2)+min(R1,R2))/2.0
            else:
                return min(R1,R2)
"""