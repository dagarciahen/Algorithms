






def test(nums, expected):
    result = next_largest_number_to_right(nums)
    print(f"nums: {nums}")
    print(f"expected: {expected}")
    print(f"result {result}")

    assert result == expectedprint("PASS\n")


test(nums, expected)
