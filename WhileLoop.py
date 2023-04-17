# Read input as sepcified in the question
# Print output as specified in the question
n = int(input())
sum=0
count=1
while (count<=n):
    sum= sum + count
    count+=1
print(sum)

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
sum=0
count=1
while (count<=N):
    if count%2==0:
        sum=sum+count
    count+=1
print(sum)

## Checking prime no.
n=int(input())
i=2
flag= False
while (i<n):
    if(n%i==0):
        flag=True
        break
    i+=1
if flag:
    print("n is not a prime no.")
else:
    print("it's a prime no.")

##Another way
n = int(input())
i = 2
is_prime = True  # flag variable to keep track of whether n is prime
while i < n:
    if n % i == 0:
        is_prime = False  # n is not prime, update flag variable
        print("not a prime no.")
        break  # exit loop early, since we already know n is not prime
    i += 1

if is_prime:
    print("n is a prime no.")

