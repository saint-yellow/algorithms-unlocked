def linear_search(A, n, x):
    answer = None
    for i in range(n):
        if A[i] == x:
            answer = i
        else:
            continue
    return answer


def better_linear_search(A, n, x):
    answer = None
    for i in range(n):
        if A[i] == x:
            answer = i
            return answer
        else:
            continue
    return answer
