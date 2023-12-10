'''1. Fahrenheit to Celsius Function
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),
you need to convert all Fahrenheit values from Start to End at the gap of W.
into their corresponding Celsius values and print the table.
    Output Format:
    Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value.
    Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")
Sample Input 1:
0
100
20
Sample Output 1:
0 -17
20 -6
40  4
60 15
80 26
100 37'''

def printTable(start, end, step):
    for i in range(s, e + 1, 20):
        F = i + s
        C= int((5 / 9)* (F - 32))
        #print(C)
        print (i,"\t",C)
    pass


s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)

'''Fibonacci Member
Given a number N, figure out if it is a member of fibonacci series or not. 
Return true if the number is member of fibonacci series else false.

Note:
Fibonacci series is the series of numbers where each number is obtained by adding two previous numbers.
The first two numbers in the Fibonacci series are 0 and 1.

Input Format:
Integer N

Output Format:
true or false
'''


def checkMember(n):
#Implement Your Code Here
    a,b=0,1
    for i in range (n+1):
        c=a+b
        a=b
        b=c
        if c==n:
            return True # Return True if n is found in the Fibonacci series
    return False # Return False if n is not found in the Fibonacci series

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")


'''Find Palindrome and check return true or false as an output '''
n=int(input())
# taking n as a input
## write your code !!
def checkPalindrome(num):
    num=n
    reverse=0
    while (num!=0):
        remainder=num%10
        reverse=reverse*10+remainder
        num=num//10
    return reverse

reverse=checkPalindrome(n)
if (reverse ==n):
    print('true')
else:
    print('false')


'''
Check Armstrong
Send Feedback
You are given an integer 'n'.
Return 'true' if 'n' is an Armstrong number, and 'false' otherwise.
Note:
An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal to the number itself. For example, 371 is an
Armstrong number because 3^3 + 713 + 1^3 = 371.
Example:
Input: 'n' = 1634
Output: true
Explanation:
1634 is an Armstrong number, as 114 + 6^4 + 3^4 +
4^4 = 1634
Input Format :
The first line of the input contains an integer 'n'.
Output Format:
Return 'true' or 'false' as mentioned in the problem statement '''

def countDigit(n):
    power= len(str(n))
    return power

def armstrongCheck(n,power):
    result=0
    while (n!=0):
        num=n%10
        result=result+num**power
        n=n//10
    return result

n = int (input())

power= countDigit(n)
result = armstrongCheck(n,power)
if (result==n):
    print('true')
else:
    print('false')



