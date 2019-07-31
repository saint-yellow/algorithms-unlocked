def count_keys_equal(A, n, m):
    equal = [0] * m
    for i in range(n):
        key = A[i]
        equal[key] += 1
    return equal


def count_key_less(equal, m):
    less = [0] * m
    for j in range(1, m):
        less[j] = less[j-1] + equal[j-1]
    return less


def rearrange(A, less, n, m):
    B = [0] * (n+1) 
    next = [0] * m 
    for j in range(m):
        next[j] = less[j] + 1
    for i in range(n):
        key = A[i]
        index = next[key]
        B[index] = A[i]
        next[key] += 1
    return B[1:]


def counting_sort(A):
    n = len(A)
    m = max(A) + 1
    equal = count_keys_equal(A, n, m)
    less = count_key_less(equal, m)
    B = rearrange(A, less, n, m)
    return B



if __name__ == '__main__':
    A = [4,1,5,0,1,6,5,1,5,3,7]
    print("A: ", A)
    B = counting_sort(A)
    print("B: ", B)

