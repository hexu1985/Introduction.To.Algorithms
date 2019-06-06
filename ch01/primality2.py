import random
import time
import modexp

def primality2(N):
    '''
    Input: Positive integer N
    Output: yes/no
    '''
    # Pick a positive integer a1, a2, ..., ak < N at random
    k = 8
    for i in range(8):
        random.seed(time.time())
        a = random.randint(1, N-1)
        if modexp.modexp(a, N-1, N) == 1:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    def test_primality2(N):
        if primality2(N):
            print("%d is pass primality test" % N)
        else:
            print("%d is not pass primality test" % N)

    test_primality2(341)
    test_primality2(499)

