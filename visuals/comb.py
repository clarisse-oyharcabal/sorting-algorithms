from visuals.base import VisualSort

class CombSortVisualizer(VisualSort):
    def sort_generator(self):
        gap = len(self.data)
        shrink = 1.3
        sorted = False

        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True

            for i in range(len(self.data) - gap):
                self.draw_list({i: "compare", i + gap: "compare"})
                yield
                if self.data[i] > self.data[i + gap]:
                    self.data[i], self.data[i + gap] = self.data[i + gap], self.data[i]
                    sorted = False
                    self.draw_list({i: "swap", i + gap: "swap"})
                    yield

        self.draw_list()
