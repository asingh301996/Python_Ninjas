'''Code : Inverted Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
333
22
1
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
55555
4444
333
22
1'''
# Read input as specified in the question
# Print the required output in given format
N = int(input())

n=1
while n<=N:
    j=1
    while j<=(N-n+1):
        print((N-n+1), end='')
        j+=1
    print( )
    n+=1

'''*********************************************************************'''
'''Code : Inverted Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
   *
  **
 ***
****
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1:
4
Sample Output 1:
   *
  **
 ***
****
'''
N = int(input())


n=1
while n<=N:
    spaces=1
    stars=1
    while spaces<= (N-n):
        print( " ", end='')
        spaces+=1
    while stars<= n:
        print('*', end='' )
        stars+=1
    print( )
    n+=1

'''*********************************************************************'''
'''Code : Mirror Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4




The dots represent spaces.


Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
3
Sample Output 1:
      1 
     12
    123
Sample Input 2:
4
Sample Output 2:
      1 
     12
    123
   1234'''

a= [[1,2,3],[4,5,6],[7,8,9]]
b=list(a)
a.append('10')
a[1][0]='N'
print(b)

N= int (input())
n=1
while n<=N:
    spaces=1
    #code for spaces
    while spaces <=(N-n):
        print (' ',end='')
        spaces+=1
    p = 1
    j=1
    #code  for increasing sequence
    while j<=n:
        print(j,end='')
        j+=1
    #decreasing Sequence
    p=n-1
    while p>=1:
        print(p, end='')
        p=p-1
    print()
    n+=1

'''  Code : Star Pattern
Send Feedback
Print the following pattern
Pattern for N = 4



The dots represent spaces.



Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1 :
3
Sample Output 1 :
   *
  *** 
 *****
Sample Input 2 :
4
Sample Output 2 :
    *
   *** 
  *****
 *******   '''

# Read input as specified in the question.
#Print output as specified in the question.

N = int(input())
n = 1

while n <= N:
    spaces = 1
    stars = 1

    # printing spaces
    while spaces <= (N - n):
        print(' ', end="")
        spaces += 1
    # #printing inc. sequence
    # while stars<=n:
    #     print('*', end=' ')
    #     stars=stars+1
    # #printing decreasing sequence
    # p=n-1
    # while p<=1:
    #      print("*", end="")
    #      p=p-1
    # print( )
    # n=n+1
    while stars <= ((2 * n) - 1):
        print('*', end='')
        stars = stars + 1
    print()
    n = n + 1

'''
Print the following pattern for the given number of rows.
Pattern for N = 4
The dots represent spaces.

Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
          232
         34543
        4567654
       567898765
Sample Input 2:
4
Sample Output 2:
          1
         232
        34543
       4567654
'''

N = int(input())
i = 1

while i <= N:
    spaces = 1
    j = 1
    p = 1
    # printing spaces
    while spaces <= (N - i):
        print(' ', end=" ")
        spaces += 1
    # increasing order
    while j <=i:
        print(i+j-1, end = ' ')
        j+=1
    #  decreasing order
    p=i-1
    while p>=1:
        print(i+p-1,end=' ')
        p-=1

    print()
    i = i + 1
########################################################################
'''Code : Diamond of stars
Send Feedback
Print the following pattern for the given number of rows.
Note: N is always odd.

Pattern for N = 5
The dots represent spaces.
Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *   '''



## Read input as specified in the question.
## Print output as specified in the question.
N = int(input())

# Upper half of the pattern
i = 1
while i <= (N + 1) // 2:
    spaces = 1
    while spaces <= ((N + 1) // 2 - i):
        print(" ", end="")
        spaces += 1

    stars = 1
    while stars <= (2 * i - 1):
        print("*", end="")
        stars += 1

    print()
    i += 1

# Lower half of the pattern
i = (N - 1) // 2
while i >= 1:
    spaces = 1
    while spaces <= ((N + 1) // 2 - i):
        print(" ", end="")
        spaces += 1

    stars = 1
    while stars <= (2 * i - 1):
        print("*", end="")
        stars += 1

    print()
    i -= 1

'''Number Pattern
Send Feedback
Print the following pattern for n number of rows.
Note: each line consist of equal number of characters + spaces. 
Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, 
again (n-x) spaces followed by x..1
For eg. N = 5 
Your Output
1        1
12      21
123    321
1234  4321
1234554321

Expected Output
1        1
12      21
123    321
1234  4321
1234554321'''


N=int(input())
i=1
while i<=N:
    p=1
    while p<=i:
        print(p, end='')
        p+=1

    spaces=1
    while spaces<=(N-i):
        print('  ',end='')
        spaces+=1
    j=i
    while j>=1:
        print(j, end='')
        j-=1

    print()
    i=i+1

'''Zeros and Stars Pattern
Send Feedback
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000 '''

n = int(input())  # no. of rows
columns = 2 * n + 1
i = 1

while i <= n:
    j = 1
    while j <= columns:
        if (j == i or j == (columns // 2 + 1) or j == columns - i + 1):
            print('*', end='')

        else:
            print('0', end='')

        j = j + 1

    print()
    i = i + 1


'''Pyramid Number Pattern
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
        1
       212
      32123
     4321234
    543212345  '''

# Read input as specified in the question.
# Print output as specified in the question.
N = int(input())
i = 1

while i <= N:
    spaces = 1
    p = 1
    # printing spaces
    while spaces <= (N - i):
        print(' ', end="")
        spaces += 1
    # decreasing order
    j=i
    while j>=1:
        print(j,end='')
        j-=1
    #  increasing order
    p=2
    while p <=i:
        print(p, end = '')
        p+=1
    print()
    i = i + 1

'''
Arrow pattern
Send Feedback
Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.
Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
11
Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
'''
N = int(input())
n1=(N + 1) // 2
n2= N // 2

# Upper half of the pattern
i = 1
while i <= n1:
    spaces = 1
    while spaces <= (i-1):
        print(" ", end="")
        spaces += 1

    stars = 1
    while stars <= i:
        print("* ", end="")
        stars += 1

    print()
    i += 1

# Lower half of the pattern
i = 1
while i <=n2:

    spaces = 1
    while spaces <=(n2-i):
        print(" ", end="")
        spaces += 1

    stars = 1
    while stars <= (n2-i+1):
        print("* ", end="")
        stars += 1

    print()
    i += 1

