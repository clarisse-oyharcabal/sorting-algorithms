import random
from sorting import SortingAlgorithm

def generate_random_list(size, min_value=0, max_value=50000):
    return [random.randint(min_value, max_value) for _ in range(size)]

def main():
    print("Bienvenue dans le comparateur d'algorithmes de tri !\n")

    size = int(input("Entrez la taille de la liste à trier : "))

    random_list = generate_random_list(size)
    
    algorithms = {
        #Ajouter les autres
        "6": ("Tri par tas", SortingAlgorithm.heap_sort),
        "7": ("Tri à peigne", SortingAlgorithm.comb_sort)
    }

    print("\nChoisissez l'algorithme de tri :")
    for key, (name, _) in algorithms.items():
        print(f"{key}. {name}")

    choice = input("\nVotre choix : ")

    if choice not in algorithms:
        print("Choix invalide. Veuillez relancer le programme.")
        return

    algo_name, algo_function = algorithms[choice]

    print(f"\nVous avez choisi : {algo_name}")

    sorter = SortingAlgorithm(random_list.copy())
    duration = algo_function(sorter)

    print("\nListe triée :")
    print(sorter.arr[:100])

    print(f"\nTemps d'exécution ({algo_name}) : {duration:.6f} secondes")

if __name__ == "__main__":
    main()
