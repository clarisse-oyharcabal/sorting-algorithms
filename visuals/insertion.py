from visuals.base import VisualSort

class InsertionSortVisualizer(VisualSort):
    def sort_generator(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                self.draw_list({j: "compare", j + 1: "swap"})
                yield
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
            self.draw_list({j + 1: "swap"})
            yield
        self.draw_list()
