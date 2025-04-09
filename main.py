import time
from sorting import (
    selection_sort,
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    comb_sort
)

def print_menu():
    print("\n=== Les Papyrus de Héron – Outil de Tri ===")
    print("1. Tri par sélection")
    print("2. Tri à bulles")
    print("3. Tri par insertion")
    print("4. Tri fusion")
    print("5. Tri rapide")
    print("6. Tri par tas")
    print("7. Tri à peigne")
    print("0. Quitter")

def get_algorithm(choice):
    algos = {
        "1": selection_sort,
        "2": bubble_sort,
        "3": insertion_sort,
        "4": merge_sort,
        "5": quick_sort,
        "6": heap_sort,
        "7": comb_sort
    }
    return algos.get(choice, None)

def main():
    while True:
        print_menu()
        choice = input("Choisissez un algorithme (1-7) ou 0 pour quitter : ")

        if choice == "0":
            print("À bientôt, jeune érudit ! 📜")
            break

        algo = get_algorithm(choice)
        if algo is None:
            print("⛔ Choix invalide. Veuillez réessayer.")
            continue

        try:
            user_input = input("Entrez une liste de nombres réels séparés par des espaces : ")
            numbers = [float(x) for x in user_input.strip().split()]
        except ValueError:
            print("⛔ Entrée invalide. Veuillez entrer uniquement des nombres.")
            continue

        start_time = time.time()
        sorted_list = algo(numbers)
        end_time = time.time()
        duration = end_time - start_time

        print(f"\n✅ Liste triée : {sorted_list}")
        print(f"⏱️ Temps d'exécution : {duration:.6f} secondes")

if __name__ == "__main__":
    main()