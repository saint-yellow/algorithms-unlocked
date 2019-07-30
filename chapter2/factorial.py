def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def bad_recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return bad_factorial(n+1) / (n+1)


def iterative_factorial(n):
    if n == 0:
        return 1
    else:
        answer = 1
        i = 1:
        while i <= n:
            answer *= i
            i += 1
        return answer
