"""Write a program that performs a binary search of a sorted array.
"""

def binary_search(target, items):
    "Return true if needle is in sorted_list, else return false."
    lower, upper = 0, len(items) - 1
   
    while lower <= upper:
        middle = lower + (upper-lower) // 2
        if items[middle] == target:
            return True
        elif items[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1
    return False

if __name__ == "__main__":
    items = range(11)
    target = 1
    print(f"The number {target} is in {items}: {binary_search(target, items)}")

    items = range(11)
    target = 12
    print(f"The number {target} is in {items}: {binary_search(target, items)}")
