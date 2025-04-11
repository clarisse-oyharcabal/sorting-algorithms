import time

class SortingAlgorithm:
    def __init__(self, arr):
        self.arr = arr

    def comb_sort(self):
        start_time = time.time()
        n = len(self.arr)
        gap = n
        shrink = 1.3  #Facteur de rétrécissement basique
        sorted = False

        while not sorted:
            gap = int(gap / shrink) #Mise à jour de l'écart
            if gap <= 1:
                gap = 1 #Quand le gap est de 1 et qu’aucun échange n’est effectué pendant une boucle, le tableau est trié
                sorted = True

            for i in range(n - gap): #Comparaison et échange
                if self.arr[i] > self.arr[i + gap]:
                    self.arr[i], self.arr[i + gap] = self.arr[i + gap], self.arr[i]
                    sorted = False  #Si un échange a été fait, ce n’est pas encore trié
        
        end_time = time.time()
        duration = end_time - start_time
        return duration