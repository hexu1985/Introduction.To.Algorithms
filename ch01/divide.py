def divide(x, y):
    '''
    Input: Two n-bit integers x and y, where y >= 1
    Output: The quotient and remainder of x divided by y
    '''
    if x == 0: return (0, 0)
    q, r = divide(x//2, y)
    q = 2 * q
    r = 2 * r
    if x % 2 == 1:  # x is odd
        r = r + 1
    if r >= y:
        r = r - y
        q = q + 1
    return (q, r)

if __name__ == '__main__':
    print("%d / %d = %d ... %d" % (103, 15, 103 // 15, 103 % 15))
    print("divmod(%d, %d) = (%d, %d)" % ((103, 15) + divmod(103, 15)))
    print("divide(%d, %d) = (%d, %d)" % ((103, 15) + divide(103, 15)))
#    q, r = divide(103, 15)
#    print("divide(%d, %d) = (%d, %d)" % (103, 15, q, r))
    
