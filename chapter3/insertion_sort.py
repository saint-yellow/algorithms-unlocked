def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key


if __name__ == '__main__':
    A = [12, 9, 3, 7, 14, 11]
    print(A)
    insertion_sort(A)
    print(A)
