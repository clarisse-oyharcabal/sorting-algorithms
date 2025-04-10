import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

def generate_random_list(size=200, lower=0, upper=1000):
    return [round(random.uniform(lower, upper), 2) for _ in range(size)]

def main():
    print("🔽 Sorting Program (Auto-Generated List of 200 Numbers)")
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")

    choice = input("Your choice (1 or 2): ")

    # Automatically generate the list
    user_list = generate_random_list()
    print("\nGenerated list (first 20 numbers):", user_list[:20], "...\n")

    if choice == "1":
        print("Using Bubble Sort...")
        sorted_list = bubble_sort(user_list)
    elif choice == "2":
        print("Using Insertion Sort...")
        sorted_list = insertion_sort(user_list)
    else:
        print("❌ Invalid choice.")
        return

    print("✅ Sorted list (first 20 numbers):", sorted_list[:20], "...\n")
    print("✅ List length:", len(sorted_list))

if __name__ == "__main__":
    main()

