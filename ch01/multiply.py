def multiply(x, y):
    '''
    Input: Two n-bit integers x and y, where y >= 0
    Output: Their product
    '''
    if y == 0: return 0
    z = multiply(x, y//2)
    if y % 2 == 0:  # y is even
        return 2*z
    else:
        return x+2*z

if __name__ == '__main__':
    print("%d * %d = %d" % (15, 24, 15 * 24))
    print("multiply(%d, %d) = %d" % (15, 24, multiply(15, 24)))
    
