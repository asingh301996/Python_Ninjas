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



