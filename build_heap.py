# python3
from sys import stdin
from math import log

def build_heap(data):
    # parent, left_child, right_child shortcuts to simplify code
    parent = lambda i: int((i-1)/2)
    left_child = lambda i: 2*i+1
    right_child = lambda i: 2*i+2

    swaps = []

    # start from end sifting up
    i = len(data)-1
    while i >= 2**int(log(len(data), 2)-1):
        sift_i = i
        sift_p = parent(i)
        while (sift_i > -1) and (data[sift_i] < data[sift_p]):#sift up
            swaps.append((sift_p, sift_i))
            data[sift_i], data[sift_p] = data[sift_p], data[sift_i]
            sift_i = sift_p
            sift_p = parent(sift_i)
        i -= 1
    return swaps


def main():
    mode = input()
    f = None

    TEST_FOLDER = "./tests/"
    if "I" in mode: # read from stdin
        f = stdin
    elif "F" in mode: # read from file
        f = open(TEST_FOLDER + input())
    else:
        exit()

    # read from chosen method
    n = int(f.readline())
    data = list(map(int, f.readline().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # get swaps to achieve heap
    swaps = build_heap(data)

    # make sure our swapping is efficient
    assert len(swaps) <= 4*n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    

if __name__ == "__main__":
    main()
