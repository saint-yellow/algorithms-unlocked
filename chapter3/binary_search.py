from math import floor

def iterative_binary_search(A, n, x):
    p = 0
    r = n - 1
    while p <= r:
        q = floor((p + r) / 2)
        if A[q] == x:
            return q
        elif A[q] > x:
            r = q - 1
        else:
            p = q + 1
    return None


def recursive_binary_search(A, p, r, x):
    if p > r:
        return None
    else:
        q = floor((p + r) / 2)
        if A[q] == x:
            return q
        elif A[q] > x:
            return recursive_binary_search(A, p, q-1, x)
        else:
            return recursive_binary_search(A, q+1, r, x)
