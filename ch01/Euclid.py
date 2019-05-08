def Euclid(a, b):
    '''
    Input: Two integers a and b with a >= b >= 0
    Output: gcd(a, b)
    '''
    if b == 0: return a
    return Euclid(b, a % b)

if __name__ == '__main__':
    def my_gcd(a, b):
        if a > b:
            return Euclid(a, b)
        else:
            return Euclid(b, a)

    import math

    print("my_gcd(%d, %d) = %d" % (1035, 759, my_gcd(1035, 759)))
    print("math.gcd(%d, %d) = %d" % (1035, 759, math.gcd(1035, 759)))   # only work in python 3

