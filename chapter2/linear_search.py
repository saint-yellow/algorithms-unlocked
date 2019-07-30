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


def sentinel_linear_search(A, n, x):
    A[n-2] = last
    A[n-1] = x
    i = 1
    while A[i] != x:
        i += 1
    A[n-1] = last
    if i < n or A[n-1] == x:
        return i
    else:
        return None


def recursive_linear_search(A, n, i, x):
    if i > n:
        return None
    elif i <= n:
        if A[i] == x:
            return i
        else:
            return recursive_linear_search(A, n, i+1, x)
