import sys
n, W = map(int, sys.stdin.readline().split());
items = []
for line in sys.stdin:
    v, w = map(int, line.split());
    items.append((v ,w));

def SortItem(items):
    items = items.copy();
    itemsSorted = [];
    while items:
        maxValueperW = -1
        best_item = None
            
        for v, w in items:
            if v/w > maxValueperW:
                maxValueperW = v/w
                best_item = (v,w)
        itemsSorted.append(best_item)
        items.remove(best_item)
    return itemsSorted

items = SortItem(items)
def Knapstack(W, n, items):
    totalValue = 0.0
    amounts = []
    for i in range(n):
        if W == 0:
            return (totalValue, amounts)
        a = min(items[i][1], W)
        totalValue = totalValue + a*items[i][0]/items[i][1]
        amounts.append(a)
        W = W - a
    return (totalValue, amounts)

print(Knapstack(W,n, items))

    

