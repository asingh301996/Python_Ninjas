## Checking prime no.
# n=int(input())
# i=2
# flag= False
# while (i<n):
#     if(n%i==0):
#         flag=True
#         break
#     i+=1
# if flag:
#     print("n is not a prime no.")
# else:
#     print("it's a prime no.")
#
# ##Another way---> Method 2
# n = int(input())
# i = 2
# is_prime = True  # flag variable to keep track of whether n is prime
# while i < n:
#     if n % i == 0:
#         is_prime = False  # n is not prime, update flag variable
#         print("not a prime no.")
#         break  # exit loop early, since we already know n is not prime
#     i += 1
#
# if is_prime:
#     print("n is a prime no.")
#
# ## Checking all th enumber which are prime till no. n


n = int(input())
k=2
flag=False
while(k<n):
    if (n%k==0):
        flag=True
    k=k+1
if flag:
    print("no. is not a prime")
else:
    print("is a prime no")
