class SortingAlgorithm: 
    def __init__ (self, arr) : 
        self.arr = arr 

    def selection_sort(self):
        arr = self.arr  # On travaille directement sur l’attribut

        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr  # Optionnel : retourne la liste triée