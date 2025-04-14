import threading
import time
from sorting import SortingAlgorithms

class SortingAppLauncher:
    def __init__(self):
        self.algos = SortingAlgorithms()

        self.algo_methods = {
            "Tri par sélection": self.algos.selection_sort,
            "Tri à bulles": self.algos.bubble_sort,
            "Tri par insertion": self.algos.insertion_sort,
            "Tri fusion": self.algos.merge_sort,
            "Tri rapide": self.algos.quick_sort,
            "Tri par tas": self.algos.heap_sort,
            "Tri à peigne": self.algos.comb_sort
        }

    def run_interface(self):
        from graphical import main as graphical_main
        graphical_main()

    def run_benchmarks(self):
        import random
        from copy import deepcopy

        data = [random.uniform(0, 100) for _ in range(30)]
        print("📜 Liste initiale :", [round(x, 2) for x in data])
        print("🔬 Résultats :")

        for name, func in self.algo_methods.items():
            to_sort = deepcopy(data)
            start = time.time()
            sorted_list = func(to_sort)
            end = time.time()
            print(f"✅ {name} → {round(end - start, 5)} s → {sorted_list}")

    def start(self):
        interface_thread = threading.Thread(target=self.run_interface)
        interface_thread.start()

        self.run_benchmarks()

        interface_thread.join()

if __name__ == "__main__":
    launcher = SortingAppLauncher()
    launcher.start()
