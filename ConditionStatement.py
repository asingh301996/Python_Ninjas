x = 5
if x < 6:
    print("Hello")
if x == 5:
    print("Hi")
else:
    print("Hey")

# Read input as sepcified in the question
# Print output as specified in the question
n= int(input())
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")

#IF ELSE Types
### Type II
m=int(input())
n= int(input())
if m%2==0:
    print("m is even")
    if n%5==0:
        print(1)
else:
#     print(3)

if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
       print('B')
    else:
      print('C')
else:
     print('D')



