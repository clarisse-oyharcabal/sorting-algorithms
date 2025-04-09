from visuals.base import VisualSort

class MergeSortVisualizer(VisualSort):
    def sort_generator(self):
        yield from self._merge_sort(0, len(self.data) - 1)
        self.draw_list()

    def _merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            yield from self._merge_sort(left, mid)
            yield from self._merge_sort(mid + 1, right)
            yield from self._merge(left, mid, right)

    def _merge(self, left, mid, right):
        left_part = self.data[left:mid + 1]
        right_part = self.data[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            self.draw_list({k: "compare"})
            yield
            if left_part[i] <= right_part[j]:
                self.data[k] = left_part[i]
                i += 1
            else:
                self.data[k] = right_part[j]
                j += 1
            self.draw_list({k: "swap"})
            yield
            k += 1

        while i < len(left_part):
            self.data[k] = left_part[i]
            i += 1
            self.draw_list({k: "swap"})
            yield
            k += 1

        while j < len(right_part):
            self.data[k] = right_part[j]
            j += 1
            self.draw_list({k: "swap"})
            yield
            k += 1
