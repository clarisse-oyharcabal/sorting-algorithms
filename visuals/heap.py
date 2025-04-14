from visuals.base import VisualSort

class HeapSortVisualizer(VisualSort):
    def sort_generator(self):
        n = len(self.data)
        for i in range(n // 2 - 1, -1, -1):
            yield from self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self.draw_list({0: "swap", i: "swap"})
            yield
            yield from self.heapify(i, 0)

        self.draw_list()

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.data[l] > self.data[largest]:
            largest = l
        if r < n and self.data[r] > self.data[largest]:
            largest = r
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.draw_list({i: "swap", largest: "swap"})
            yield
            yield from self.heapify(n, largest)
