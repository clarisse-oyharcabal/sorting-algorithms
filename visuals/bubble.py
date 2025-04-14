from visuals.base import VisualSort

class BubbleSortVisualizer(VisualSort):
    def sort_generator(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.draw_list({j: "compare", j + 1: "compare"})
                yield
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_list({j: "swap", j + 1: "swap"})
                    yield
        self.draw_list()
