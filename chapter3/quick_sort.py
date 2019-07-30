def recursive_quick_sort(A, p, r):
    if p >= r:
        return
    else:
        q = partition(A, p, r)
        recursive_quick_sort(A, p, q - 1)
        recursive_quick_sort(A, q + 1, r)


def partition(A, p, r):
    q = p
    for u in range(p, r):
        if A[u] <= A[r]:
            A[q], A[u] = A[u], A[q]
            q += 1
    A[q], A[r] = A[r], A[q]
    return q


if __name__ == '__main__':
    A = [12, 9, 3, 7, 14, 11]
    n = len(A)
    p = 0
    r = n - 1
    print(A)
    recursive_quick_sort(A, p, r)
    print(A)
