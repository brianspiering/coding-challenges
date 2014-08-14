""" Write a program that does a binary search of a sorted array.
"""
from __future__ import division

def binary_search(needle, sorted_list):
    "Return true if needle is in sorted_list, else return false."

    if sorted_list != sorted(sorted_list): # Make sure list is sorted
        sorted_list = sorted(sorted_list)

    left, right = 0, len(sorted_list)-1
    while left < right:
        midpoint = (left+right)//2
        if needle == sorted_list[midpoint]:
            return True
        elif needle < sorted_list[midpoint]:
            right = midpoint-1
        else:
            left = midpoint+1
    return False # Needle in sorted array

if __name__ == "__main__":
    sorted_list = xrange(11)
    needle = 7
    print("The number {0} is in {1}: {2}".
        format(needle, sorted_list, binary_search(needle, sorted_list)))