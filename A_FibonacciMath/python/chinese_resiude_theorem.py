import sys
k = sys.stdin.readline().split()
numbers = []
for i in range(k):
    x, n = map(int, sys.stdin.readline().split())
    numbers.append((x, n))

def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
        
def check_pairwise(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, range(len(numbers))):
            n1 = numbers[i][1]
            n2 = numbers[j][1]
            gcdNum = gcd(n1,n2)
            if gcdNum != 1:
                print(f"{n1} and {n2} are not pairwiserelatively")
                return False
    print("all ni are pairwise relatively")
    return True

def ChineseResidueTheorem(numbers):
    if check_pairwise(numbers):
        nprList = []
        sumofn = 0
        for x, n in numbers:
            sumofn += n
        #sumofn = sum(n for _, n in numbers)
        for x, n in numbers:
            npr = n/sumofn
            nprList.append(npr)

            

                       

