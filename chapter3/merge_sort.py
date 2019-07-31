from math import floor


def recursive_merge_sort(A, p, r):
    if p >= r:
        return A
    else:
        q = floor((p + r) / 2)
        recursive_merge_sort(A, p, q)
        recursive_merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    B = A[p:q+1]
    B.append(1024)
    C = A[q+1:r+1]
    C.append(1024)
    i, j = 0, 0
    for k in range(p, r+1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
    return A


if __name__ == '__main__':
    A = [12, 9, 3, 7, 14, 11]
    n = len(A)
    p = 0
    r = n - 1
    print(A)
    recursive_merge_sort(A, p, r)
    print(A)
