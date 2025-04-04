class SortingAlgorithm : 
    def __init__ (self, arr) : 
        self.arr = arr 
    def merge(self, left, right):
        """Fusionne deux listes triées en une seule liste triée."""
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(self, arr):
        """Implémente l'algorithme de tri fusion."""
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)