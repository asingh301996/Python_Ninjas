'''Print checking the prime no. '''

def chkPrime(n):
    for i in range (2, n):
        if (n % i == 0):
            break
    else:
        return True
    return False
#
# chkPrime(2)
# print (chkPrime(2))

'''Print all prime no. 1 to n'''
def primeFrom2toN(n):
    for k in range(2, n + 1):
        # check if k is prime
        is_k_prime = chkPrime(k)
        # print only if k is prime and odd
        if is_k_prime:
            print(k)

primeFrom2toN(20)

'''Function for calculating nCr'''


def fact(a):
    a_fact = 1
    for i in range(1, a + 1):
        a_fact = a_fact * i
    return a_fact
def ncr(n,r):
    n_fact = fact(n)
    r_fact = fact(r)
    n_r_fact = fact(n - r)
    ans = n_fact // (r_fact * n_r_fact)
    return (ans)

ncr(5,2)
print (ncr(5,2))

