def extended_Euclid(a, b):
    '''
    Input: Two positive integers a and b with a >= b >= 0
    Output: Integers x,y,d such that d = gcd(a, b) and a*x + b*y = d
    '''
    if b == 0: return (1, 0, a)
    x1, y1, d = extended_Euclid(b, a % b)
    return (y1, x1 - (a//b)*y1, d)

if __name__ == '__main__':
    def my_gcd(a, b):
        if a > b:
            return extended_Euclid(a, b)
        else:
            return extended_Euclid(b, a)

    a = 25; b = 11
    x, y, d = my_gcd(a, b)
    print("my_gcd(%d, %d) = %d, (%d)*(%d) + (%d)*(%d) = %d" % (a, b, d, a, x, b, y, d))

