def bubble_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

def insertion_sort(arr):
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

if __name__ == "__main__":
    print("🔢 Sorting Program (Bubble Sort & Insertion Sort)")

    # Ask user for numbers
    user_input = input("Enter numbers separated by commas (e.g. 4.5, 2.1, 9.8): ")
    try:
        # Convert input to list of floats
        user_list = [float(num.strip()) for num in user_input.split(",")]

        print("\nOriginal list:", user_list)

        bubble_result = bubble_sort(user_list)
        print("✅ Sorted with Bubble Sort:", bubble_result)

        insertion_result = insertion_sort(user_list)
        print("✅ Sorted with Insertion Sort:", insertion_result)

    except ValueError:
        print("❌ Invalid input. Please enter only numbers separated by commas.")
