import time

class SortingAlgorithm:
    def __init__(self, arr):
        self.arr = arr

    def heap_sort(self):
        """Echange l'élément racine (le plus grand) avec le dernier et l'ignore ensuite"""
        start_time = time.time()
        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1): # Max heap
            self._heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]  # Échanger
            self._heapify(i, 0)

        end_time = time.time()
        return end_time - start_time

    def _heapify(self, n, i):
        """Méthode pour réorganiser les éléments de bas en haut (largest en haut)"""
        largest = i  # Racine actuelle
        left = 2 * i + 1  # Fils gauche
        right = 2 * i + 2  # Fils droit

        
        if left < n and self.arr[left] > self.arr[largest]: # Voir si le fils gauche existe et est plus grand que la racine
            largest = left

        if right < n and self.arr[right] > self.arr[largest]: # Même chose fils droit
            largest = right


        if largest != i: #Si la plus grande valeur n'est pas la racine
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]  # Échanger
            self._heapify(n, largest)

    def comb_sort(self):
        start_time = time.time()
        n = len(self.arr)
        gap = n
        shrink = 1.3  # Facteur de rétrécissement basique
        sorted = False

        while not sorted:
            gap = int(gap / shrink) # Mise à jour de l'écart
            if gap <= 1:
                gap = 1
                sorted = True

            # Compare les éléments et les échange avec l'écart actuel
            for i in range(n - gap):
                if self.arr[i] > self.arr[i + gap]:
                    self.arr[i], self.arr[i + gap] = self.arr[i + gap], self.arr[i]
                    sorted = False # Si un échange a été fait ce n'est pas encore trié

        end_time = time.time()
        return end_time - start_time
