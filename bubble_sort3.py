def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # Pythonic tuple unpacking to swap elements and flag the change in one line
                arr[j], arr[j + 1], swapped = arr[j + 1], arr[j], True
                
        print(f"Pass {i + 1}: {arr}")
        if not swapped:
            print(f"-> Sorting finished early at Pass {i + 1} because no swaps were made.")
            break
    return arr

if __name__ == "__main__":
    unsorted_list = [67, 85, 4, 1, 9, 17, 33]
    print(f"=== BUBBLE SORT DEMONSTRATION ===\nInitial Unsorted List: {unsorted_list}\n" + "-" * 40)
    
    sorted_list = bubble_sort(list(unsorted_list))
    print("-" * 40 + f"\nFinal Sorted List:     {sorted_list}")