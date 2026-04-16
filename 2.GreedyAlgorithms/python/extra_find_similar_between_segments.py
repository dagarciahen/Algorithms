import sys 
n = int(input())
segments = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    segments.append((a,b))

def calculator(segments):
    new_segments = []
    all_points = []

    for i in range(n):
        for j in range(i+1,n):
            (a1, b1 ) = segments[i]
            (a2, b2) = segments[j]
            list1 = create_list(a1,b1)
            list2 = create_list(a2,b2)
            #limits
            start = max(list1[0], list2[0])
            end = min(list1[-1], list2[-1])
            new_segments = []
            for k in range(len(list2)):
                if list2[k] >= start and list2[k] <= end:
                    new_segments.append(list2[k])
                if new_segments:
                    all_points.append(new_segments)
    return all_points


def create_list(a,b):
    lista = []
    for i in range(a,b+1):
        lista.append(i)
    return lista

print(calculator(segments))






