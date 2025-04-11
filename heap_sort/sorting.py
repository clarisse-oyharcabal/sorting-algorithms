import time

class SortingAlgorithm:
    def __init__(self, arr):
        self.arr = arr

    def heap_sort(self):
        """Echange l'élément racine (le plus grand) avec le dernier et l'ignore ensuite"""
        start_time = time.time()

        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1): #Max heap
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.heapify(i, 0)

        end_time = time.time()
        duration = end_time - start_time
        return duration

    def heapify(self, n, i):
        """Méthode pour réorganiser les éléments de bas en haut (largest en haut)"""
        largest = i        #Racine actuelle
        left = 2 * i + 1   #Fils gauche
        right = 2 * i + 2  #Fils droit
       
        if left < n and self.arr[left] > self.arr[largest]: #Si le fils gauche est plus grand que la racine
            largest = left

        if right < n and self.arr[right] > self.arr[largest]: #Si le fils droit est plus grand que le plus grand trouvé jusque-là
            largest = right

        #Si la plus grande valeur n'est pas la racine
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)
