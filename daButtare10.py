""" Write a binary search algorithm """
def binarySearch(alist, item):
    """ Binary search algorithm """
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
def main():
    """ Main function """
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binarySearch(alist, 5))
    print(binarySearch(alist, 10))
if __name__ == "__main__":
    main()

# Path: daButtare11.py
