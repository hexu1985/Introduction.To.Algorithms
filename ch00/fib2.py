def fib2(n):
    if n == 0:
        return 0
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

if __name__ == '__main__':
    print('fib2(7): %d' % fib2(7))
