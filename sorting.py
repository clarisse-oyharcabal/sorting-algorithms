class SortingAlgorithm:
    def __init__(self, data):
        self.data = data

    def quick_sort(self, array=None):
        if array is None:
            array = self.data

        if not array:
            return []

        pivot = array[-1]
        less = [x for x in array if x < pivot]
        greater_or_equal = [x for x in array[:-1] if x >= pivot]

        return self.quick_sort(less) + [pivot] + self.quick_sort(greater_or_equal)
