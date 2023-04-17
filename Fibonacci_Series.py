'''Printing the fibinacci series of Nth term'''
def fib(N):
    n1=0
    n2=1
    count=0
    if N == 1:
        return n2
    elif N==0:
        return n1
    while (count<(N-1)):  # N-1 because the loop is starting from 0
            n3=n1+n2
            n1=n2
            n2=n3
            count+=1
    return n3

Num=int(input())
print(fib(Num))

########################################################################################################################

'''Printing the fibinacci series till the Nth term'''
def fib(N):
    n1=0
    n2=1
    count=0
    if N == 1:
        print(n1)
    else:
        print(n1)
        print(n2)
    while (count<(N-2)): # N-2 because two terms are getting printed already. We need to take care of other terms than 0&1
            n3=n1+n2
            n1=n2
            n2=n3
            count+=1
            print(n3)

Num=int(input())
fib(Num)

