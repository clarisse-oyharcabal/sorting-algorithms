from visuals.base import VisualSort

class QuickSortVisualizer(VisualSort):
    def sort_generator(self):
        stack = [(0, len(self.data) - 1)]

        while stack:
            low, high = stack.pop()
            if low < high:
                pivot_index = yield from self._partition(low, high)
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))
        self.draw_list()

    def _partition(self, low, high):
        pivot = self.data[high]
        i = low - 1

        for j in range(low, high):
            self.draw_list({j: "compare", high: "compare"})
            yield
            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.draw_list({i: "swap", j: "swap"})
                yield

        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.draw_list({i + 1: "swap", high: "swap"})
        yield

        return i + 1
