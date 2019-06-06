import random
import time
import modexp

def primality(N):
    '''
    Input: Positive integer N
    Output: yes/no
    '''
    # Pick a positive integer a < N at random
    random.seed(time.time())
    a = random.randint(1, N-1)
    if modexp.modexp(a, N-1, N) == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    def test_primality(N):
        if primality(N):
            print("%d is pass primality test" % N)
        else:
            print("%d is not pass primality test" % N)

    test_primality(341) # composite number
    test_primality(499) # prime number
    test_primality(561) # carmicheal number

