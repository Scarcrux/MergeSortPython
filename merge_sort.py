def merge_sort(A, p, r):
    if (p < r):
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    # initialize loop counters
    i = 0
    j = 0
    n1 = q - p + 1
    n2 = r - q

    # create temp arrays for merges
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)

    # populate temp arrays
    for i in range(0, n1):
        L[i] = A[p + i]

    for j in range(0, n2):
        R[j] = A[q + j + 1]

    # set infinite sentinel
    L[n1] = float("inf")
    R[n2] = float("inf")

    # reset loop counters
    i = 0
    j = 0

    for k in range(p, r + 1):
        # assign the smaller element to sorted A
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

A = [2, 1, 6, 3, 4]
print("Original Array: ", A)
merge_sort(A, 0, len(A) - 1)
print("Sorted Array: " , A)
