import random

def bubble_sort(arr):
    """
    Sorts a list of numbers using the Bubble Sort algorithm.
    Prints the list state at the end of each outer loop pass.
    """
    n = len(arr)
    
    # Outer loop to access each list element
    for i in range(n):
        # Flag to track if any swapping happened in this pass (optimization)
        swapped = False
        
        # Inner loop to compare adjacent elements
        # The last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # Print the progress after each complete pass of the outer loop
        print(f"Pass {i + 1}: {arr}")
        
        # If no two elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            print(f"-> Sorting finished early at Pass {i + 1} because no swaps were made.")
            break
            
    return arr

if __name__ == "__main__":
    # Generate a list of 7 unsorted random integers between 1 and 100
    # random.sample guarantees that the 7 integers are unique for clearer visualization
    unsorted_list = random.sample(range(1, 100), 7)
    
    print("=== BUBBLE SORT DEMONSTRATION ===")
    print(f"Initial Unsorted List: {unsorted_list}")
    print("-" * 40)
    
    # Copy the list so we preserve the original for display purposes
    working_list = list(unsorted_list)
    sorted_list = bubble_sort(working_list)
    
    print("-" * 40)
    print(f"Final Sorted List:     {sorted_list}")