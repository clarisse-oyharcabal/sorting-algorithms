from sorting import SortingAlgorithm

arr = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
sorter = SortingAlgorithm(arr)
sorter.heap_sort()
print(sorter.arr)