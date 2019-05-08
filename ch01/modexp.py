def modexp(x, y, N):
    '''
    Input: Two n-bit integers x and N, an integer exponent y
    Output: x**y mod N
    '''
    if y == 0: return 1
    z = modexp(x, y // 2, N)
    if y % 2 == 0:  # y is even
        return (z * z) % N
    else:
        return (x * z * z) % N

if __name__ == '__main__':
    print("%d ** %d mod %d = %d" % (2, 11, 7, (2**11 % 7)))
    print("modexp(%d, %d, %d) = %d" % (2, 11, 7, modexp(2, 11, 7)))
