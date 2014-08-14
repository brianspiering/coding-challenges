""" Write a program that does a binary search of a sorted array.
"""

def binary_search(needle, sorted_list):
    "Return true if needle is in sorted_list."
    pass

if __name__ == "__main__":
    sorted_list = xrange(11)
    needle = 7
    print("The number {0} is in {1}: {2}".
        format(needle, sorted_list, binary_search(needle, sorted_list)))