import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

def find_majority(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    m = len(numbers) // 2
    
    
    cand_left = find_majority(numbers[0], numbers[medium-1])
    cand_right = find_majority(numbers[medium], numbers[len(numbers)-1])
    if cand_left == cand_right:
        return cand_left

    count_l = 0
    for x in numbers:
        if numbers[i] == cand_left:
            count_l += 1

    count_r = 0
    for x in numbers:
        if numbers[i] == cand_right:
            count_r += 1

    if count_l > len(numbers) // 2:
        return cand_left
    if count_rigth > len(numbers) // 2:
        return cand_right

    return none

