'''
Binary Pattern
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
1111
000
11
0
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
11111
0000
111
00
1
'''

n=int(input())

for i in range (1,n+1,1):
    for j in range (1,n-i+1+1,1):
        if i%2==0:
            print(0, end='')
        else:
            print(1,end='')
    print()

#########################################################################################################################
'''Print Number Pyramid

Print the following pattern for a given n.
For eg. N = 6
 123456
  23456
   3456
    456
     56
      6
     56
    456
   3456
  23456
 123456
Sample Input 1 :
4
Sample Output 1 :
1234
 234
  34
   4
  34
 234
1234 '''

## Read input as specified in the question.
## Print output as specified in the question.
N = int(input())

# Upper half of the pattern
for i in range(1, N + 1):
    # Print spaces
    for space in range(1, i):
        print(" ", end='')

    # Print numbers in increasing order
    for j in range(i, N + 1, 1):
        print(j, end='')

    print()

# Lower half of the pattern
for i in range(1, N):
    # Print spaces
    for space in range(1, N - i, 1):
        print(" ", end='')

    # Print numbers in increasing order
    for j in range(N - i, N + 1, 1):
        print(j, end='')

    print()

'''Diamond of Stars
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
  *'''
## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
# Upper half of the pattern
for i in range (i,((N + 1) // 2)+1 ):
   # for loop for giving space
    spaces = 1
    for spaces in range (1, ((N + 1) // 2 - i)+1):
        print(" ", end="")
        spaces += 1
    #for loop printing stars in upper half pattern
    stars = 1
    for stars in range(1, (2 * i - 1)+1):
        print("*", end="")
        stars += 1

    print()

# Lower half of the pattern
i = (N - 1) // 2
for i in range ( i,-1, -1):

    spaces = 1
    for spaces in range(spaces, ((N + 1) // 2 - i)+1):
        print(" ", end="")
        spaces += 1

    stars = 1
    for stars in range(stars, (2 * i - 1)+1):
        print("*", end="")
        stars += 1

    print()


'''Rectangular numbers
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
1111111
1222221
1233321
1234321
1233321
1222221
1111111
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
111111111
122222221
123333321
123444321
123454321
123444321
123333321
122222221
111111111'''

N = int(input())

for row in range(1, 2 * N):
    for col in range(1, 2 * N):
        # Calculate distances from each side of the matrix
        left_distance = col
        right_distance = 2 * N - col
        up_distance = row
        down_distance = 2 * N - row

        # Find the minimum of all distances
        min_distance = min(left_distance, right_distance, up_distance, down_distance)

        # Print the minimum distance for each block
        print(min_distance, end="")

    print()  # Move to the next line after printing each row

'''
Rectangular numbers
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
3
Sample Output :
33333
32223
32123
32223
33333'''

## Read input as specified in the question.
## Print output as specified in the question.
N = int(input())
row = 0
col = 0
for row in range(0, (2 * N) - 1):
    for col in range(0, (2 * N) - 1):
        # Calculate distances from each side of the matrix
        left_distance = col
        right_distance = 2 * N - col - 2
        up_distance = row
        down_distance = 2 * N - row - 2

        # Find the minimum of all distances
        min_distance = N - min(left_distance, right_distance, up_distance, down_distance)

        # Print the minimum distance for each block
        print(min_distance, end="")

    print()  # Move to the next line after printing each row

'''Print the following pattern for the given number of rows.
Pattern for N = 5
 1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
4
Sample Output :
 1  2  3  4
 9 10 11 12
13 14 15 16
 5  6  7  8'''

n = int(input( ))
P = 1
for i in range(1, n + 1):
    for j in range(P, P + n):
        print(j, end=" ")
    print()
    if i == ((n + 1)//2):
        if (n % 2) != 0:
            P = n*(n - 2) + 1
        else:
            P = n * (n - 1) + 1
    elif i > ((n + 1) // 2):
        P = P - 2 * n
    else:
        P = P + 2 * n

