# This is a quicksort algorithm that uses different ways to chose it's pivot point
# Total comps is the number of comparisons made during the sort, to compare the
# efficiency of each pivot

import random

filename = "QuickSort.txt"
f = open(filename)
numbers = [int(x) for x in f.read().splitlines()]

totalComps = 0

def quicksort(myList, part, start, end):
    """list, function, int, int -> None

    takes in a list with unique values, a function telling it how to pivot, start and end
    are index values of where to start and stop the sorting in the recursion."""

    if end - start <= 0:
        pass
    else:
        global totalComps
        totalComps += (end - start)
        pivot = partition(myList, part, start, end)
        quicksort(myList, part, start, pivot - 1)
        quicksort(myList, part, pivot + 1, end)

def partition(myList, pivotF, start, end):
    """partition function which uses the first index in the array as the pivot value"""
    
    pivotF(myList, start, end)
    pivot = myList[start]
    i = start + 1
    for j in range(start, end + 1):
        if myList[j] < pivot:
            myList[i], myList[j] = myList[j], myList[i]
            i += 1
    myList[start], myList[i-1] = myList[i-1], myList[start]
    return i - 1

def pivotFirst(myList, start, end):
    pass

def pivotLast(myList, start, end):
    myList[start], myList[end] = myList[end], myList[start]

def pivotRand(myList, start, end):
    idx = random.randint(start, end)
    myList[start], myList[idx] = myList[idx], myList[start]

def pivotMedian(myList, start, end):
    mid = ((start + end) / 2)
    values = [myList[start], myList[end], myList[mid]]
    median = sorted(values)[1]
    idx = myList.index(median)
    myList[start], myList[idx] = myList[idx], myList[start]
