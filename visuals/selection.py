from visuals.base import VisualSort

class SelectionSortVisualizer(VisualSort):
    def sort_generator(self):
        n = len(self.data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.draw_list({min_idx: "compare", j: "compare"})
                yield
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
                    self.draw_list({min_idx: "swap"})
                    yield
            if min_idx != i:
                self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
                self.draw_list({i: "swap", min_idx: "swap"})
                yield
        self.draw_list()
