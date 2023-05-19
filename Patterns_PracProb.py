'''Code : Triangular Star Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
*
**
***
****
Note : There are no spaces between the stars (*).
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
*
**
***
****
*****'''

# Read input as specified in the question
# Print the required output in given format
N=int(input())
i=1

while (i<=N):
    j = 1
    while(j<=i):

        print('*',end='')
        j += 1
    i+=1
    print()

'''Code : Triangle Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
22
333
4444
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
1
22
333
4444
55555'''


# Read input as specified in the question
# Print the required output in given format
N=int(input())
i=1
while (i<=N):
    j=1
    while(j<=i):

        print( i, end='')
        j+= 1
    print()
    i+=1

'''Code : Reverse Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
21
321
4321
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
1
21
321
4321
54321
Sample Input 2:
6
Sample Output 2:
1
21
321
4321
54321
654321'''

N=int(input())
i=1

while (i<=N):                    #
    j=1                          #
    while(j<=i):                 #
        print( i-j+1, end='')    #or
        j+=1                     #
    print()                      #
    i+=1                         #


'''ode : Interesting Alphabets
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
Input format :
N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 26
Sample Input 1:
8
Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH
Sample Input 2:
7
Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG '''

# Read input as specified in the question.
# Print output as specified in the question.
N=int(input())
i=1
ascii_targetValue = 0
while(i<=N):
    j=1
    x=chr(64+N)
    start_char=chr(ord(x)-i+1)
    while(j<=i):
        ascii_targetValue = chr(ord(start_char) + j -1)
        print(ascii_targetValue, end='')
        j+=1
    i+=1
    print()


'''Number Pattern 1

Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
111
1111
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines'''
# Read input as specified in the question.
# Print output as specified in the question.
N=int(input())
i=1

while (i<=N):
    j = 1
    while(j<=i):
        print( 1, end='')
        j+=1
    print()
    i+=1

'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
Input format :
Integer N (Total no. of rows)
Constraints:
1 <= n <= 50
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
202
3003
40004'''
# Read input as specified in the question.
# Print output as specified in the question.
# Read input as specified in the question.
# Print output as specified in the question.
N=int(input())
i=1

while (i<=N):
    j = 1
    while(j<=i):
        if i==1:
            print( 1, end='')
        elif j==1 or j==i:
            print(i-1,end='')
        else:
            print(0,end='')
        j+=1
    print()
    i+=1



'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
12345
1234
123
12
1'''

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
while (i<=N):
    j = 1
    while(j<=(N-i+1)):
        print( j, end='')
        j+=1
    print()
    i+=1



