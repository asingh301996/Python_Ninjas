'''SQUARE PATTERNS'''

'''****
   ****
   ****
   ****
Print the above pattern'''
n=int(input()) # no. of rows
i=1
while(i<=n):
    j=1
    while(j<=n): # this loop is for columns
        print('*' , end='') #it will print * in new line which we don't want we want it to print adjacently
        j+=1
    print()
    i+=1


'''Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
4444
4444
4444
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
7
Sample Output 1:
7777777
7777777
7777777
7777777
7777777
7777777
7777777
Sample Input 1:
6
Sample Output 1:
666666
666666
666666
666666
666666
666666 '''
## Read input as specified in the question
## Print the required output in given format
N=int(input())
i=1
while (i<=N):
    j=1
    while(j<=N):
        print(N, end='')
        j+=1
    print()
    i+=1

'''PRint the following pattern
1111
2222
3333
4444'''
N=int(input())
i=1
while (i<=N):
    j=1
    while j<=N:
        print(i,end='')
        j+=1
    print()
    i+=1

'''Print the following pattern
1234
1234
1234
1234'''

N=int(input())
i=1
while (i<=N):
    j=1
    while j<=N:
        print(j,end='')
        j+=1
    print()
    i+=1

'''Print the following pattern
4321
4321
4321
4321'''
N=int(input())
i=1
while (i<=N):
    j=1
    while (j<=N):
        print((N-j+1),end='')
        j+=1
    print()
    i+=1

################################################# TRIANGLE PATTERNS ######################################################################

'''TRIANGLE PATTERNS'''
'''
1      # N ROWS WHICH IS OUTER MOST LOOP
12     # HOW MANY COLUMNS IN ith row? --> ith row has i columns 
123    # j --> value will be dependent on i's value (inner loop)
1234
'''
N=int(input())
i=1
while (i<=N):
    j=1
    while (j<=i):
        print(j,end='')
        j+=1
    print()
    i+=1

'''
1      # N ROWS WHICH IS OUTER MOST LOOP
23     # HOW MANY COLUMNS IN ith row? --> ith row has i columns 
345    # j --> value will be dependent on i's value (inner loop)
4567
'''
N=int(input())
i=1
while (i<=N):
    j=1
    p = i
    while (j<=i):
        print(p,end='')  #or instead of using p, simply write i+j-1
        p+=1
        j+=1
    print()
    i+=1

'''
1      # N ROWS WHICH IS OUTER MOST LOOP
2 3     # HOW MANY COLUMNS IN ith row? --> ith row has i columns 
4 5 6    # j --> value will be dependent on i's value (inner loop)
7 8 9 10
'''
N=int(input())
i=1
p=1
while (i<=N):
    j=1
    #p=1 --> you are resetting the p's value that's why you will never get the pattern
    while (j<=i):
        print(p,end='')
        p+=1
        j+=1
    print()
    i+=1

######################################## CHARACTER PATTERN ########################################################################
'''CHARACTER PATTERN'''

''' 'ord' method gives --> ASCII value of characters 
chr(any no.) --> will give character for the corresponding 
ABCD
ABCD
ABCD
ABCD
'''
N=int(input())
i=0
x=ord('A')
ascii_targetValue = 0

while(i<N):
    j=1
    while(j<=N):
        ascii_targetValue = chr(x + j -1)
        print(ascii_targetValue, end='')
        j+=1
    i+=1
    print()

'''
Print the below pattern
ABCD
BCDE
CDEF
DEFG'''

N=int(input())
i=1

ascii_targetValue = 0

while(i<=N):
    j=1
    start_char=chr(ord('A')+i-1)
    while(j<=N):
        ascii_targetValue = chr(ord(start_char) + j -1)
        print(ascii_targetValue, end='')
        j+=1
    i+=1
    print()


'''
Print the below pattern
A
BC
CDE
DEFG'''

N=int(input())
i=1

ascii_targetValue = 0

while(i<=N):
    j=1
    start_char=chr(ord('A')+i-1)
    while(j<=i):
        ascii_targetValue = chr(ord(start_char) + j -1)
        print(ascii_targetValue, end='')
        j+=1
    i+=1
    print()

##########################################
