def selection_sort(A: list) -> None:
    n = len(A)
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            if A[j] < A[smallest]:
                smallest = j
            continue
        A[i], A[smallest] = A[smallest], A[i]

if __name__ == '__main__':
    A = [12, 9, 3, 7, 14, 11]
    print(A)
    selection_sort(A)
    print(A)
