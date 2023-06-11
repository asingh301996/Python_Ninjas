a='abcdef'

for c in a:
    print(c)

a='ANKITA'
''' i need a a sequence here ( a collection) to
# create a colletion of elements'''
for i in a:
    print(a)

if I want to print a sequence of a natural number
n =int(input())
''' range : a method which has 3 arguments
[START, STOP-1, STRIDE]
(0,n,1)-> output will be 0,1,2,3
(0,n+1,1)->output will be 0,1,2,3,4
(n+1)-> 0,1,2,3,4
By default start value = 0
By Default stride value =1'''
for i in range (n,0,-1):
    print(i)

#print multiple of 3
for i in range (1,100):
    if i%3==0:
        print(i)
    #####OR#######
given that a<b
a=int(input())
b=int(input())
if a%3==0:
    s=a
elif a%3==1:
    s=a+2
else:
    s=a+1

for i in (s,b+1,3):
    print(i)

########################################
#finding factorial

n=int(input("enter the no."))
i=1
Ans=1
for i in range (1,n+1):
    if i==0:
        print(1)
    Ans= i*Ans
    print(Ans)

#############################################

#finding prime no.

n=int(input())
Flag=False
for i in range (2,n,1):
     if n%i==0:
        Flag = True
if Flag:
    print("Not prime")
else:
    print("prime")

####################################################

#Pattern Printing
   #     1
   #   2 3 2
   #  3 4 5 4 3
   # 4 5 6 7 6 5 4

N=int(input("enter the no. of rows"))

i=1
for i in range (1,N+1,1):  # row no. going from 1 to N
    space=1
    for space in range (1,N-i+1,1):
        print(" ",end='')
    #increasing order
    for inc in range (i,2*i+1-1,1):
        print(inc, end='')
    # decreasing order
    for dec in range (2*i-2,i-1,-1):
        print(dec, end='')
    print()


###############################################################################
'''BREAK Concept'''
i=1
while i<=10:
    if i==5:
        break
    print (i)
    i+=1

'''Prime No.'''
n=int(input())
d=2
flag= False
while d<=n:
    if n%d==0:
        flag=True
        break
    d=d+1
if flag:
    print("not a prime no.")
else:
    print("prime no.")
#-------------------------------------------------
n=int(input())
Flag=False
for i in range (2,n,1):
     if n%i==0:
        Flag = True
        break
if Flag:
    print("Not prime")
else:
    print("prime")

#################### else keyword ########################################
while (condition):
    {
      break
    }
else: #(else code will not be executed if the loop is terminated with "break")
    print{"not be executed"}

#################### continue keyword ########################################
'''break is used wjhen we wanna break a loop'''
'''continue is used whe I wanna skip some iteration'''

'''Let's say I wanna orint from 1 to 101 and i don't wanna print 29 '''
for i in range (1,102,1):
    if i ==29:
        continue
    print(i, end=' ')

'''let's say I want no. from 1 to 100 '''
for i in range (1,102,1):
    if i ==29:
        continue
    if i%2==0:
        continue
    print(i, end=' ')

#################### Pass keyword ##############################################

i=3
if i<7:
    pass
print("hey")

i=2
while i<4:
    pass
    i+=1 # even if u aren't gonna write anything u need to increament i
print("hey")

for i in range (1,4):
    pass
print("hey")
