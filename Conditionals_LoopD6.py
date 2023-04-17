''''/////Fahrenheit to Celsius//////
Send Feedback
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
Input Format :
3 integers - S, E and W respectively
Output Format :
Fahrenheit to Celsius conversion table. One line for every Fahrenheit and corresponding Celsius value in integer form. The Fahrenheit value and its corresponding Celsius value should be separate by single space.
Constraints :
0 <= S <= 90
S <= E <=  900
0 <= W <= 80
Sample Input 1:
0
100
20
Sample Output 1:
0   -17
20  -6
40  4
60  15
80  26
100 37
Sample Input 2:
20
119
13
Sample Output 2:
20  -6
33  0
46  7
59  15
72  22
85  29
98  36
111 43 **//'''
#CODE TRIED
# S=int(input())
# E=int(input())
# W=int(input())
# #C = (F - 32) * 5/9
# while ( S<=E):
#     C = (S - 32) * 5/9
#     while ((S-W)<=E):
#         C= C-20
#     print(C)
'''*******AMENDED CODE********************'''
# Read input as sepcified in the question
# Print output as specified in the question
S=int(input())
E=int(input())
W=int(input())
#C = (F - 32) * 5/9
while ( S<=E):
    C = (S - 32) * 5/9
    print(S,int(C))
    S=S+W

####################################################################################################################
'''Calculator
Send Feedback
Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
3. If the input is 3, then 2 integers are taken from the user and their product is printed.
4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
6. If the input is 6, then the program exits.
7. For any other input, then print "Invalid Operation".
Note: Each answer in next line.
Input format:
Take integers as input, in accordance to the description of the question. 
Constraints:
Time Limit: 1 second
Output format:
The output lines must be as prescribed in the description of the question.
Sample Input:
3
1
2
4
4
2
1
3
2
7
6
Sample Output:
2
2
5
Invalid Operation
'''

# TRIED CODE
# while(n<=6):
#     if(n==1):
#             x=int(input())
#             y=int(input())
#             print(x+y)

#     elif(n==2):
#             x=int(input())
#             y=int(input())
#             print(x-y)

#     elif(n==3):
#             x=int(input())
#             y=int(input())
#             print(x*y)

# #     elif(n==4):
# #             x=int(input())
# #             y=int(input())
# #             print(x//y)
#
# #     elif(n==5):
# #             x=int(input())
# #             y=int(input())
# #             print(x%y)
#
# #     elif(n==6):
# #         quit()
#
# #     else:
# #         print("invalid operation")
#
'''AMENDED CODE'''
# ansArr = []
# ansArr.append(2+3)
# print(ansArr)
a = int(input())
while (a != 6):
    if (a == 1):
        x = int(input())
        y = int(input())
        print(x + y)
        # print("works 1")

    elif (a == 2):
        x = int(input())
        y = int(input())
        print(x - y)
        # print("works 2")

    elif (a == 3):
        x = int(input())
        y = int(input())
        print(x * y)
        # print("works 3")

    elif (a == 4):
        x = int(input())
        y = int(input())
        print(int(x / y))
        # print("works 4")

    elif (a == 5):
        x = int(input())
        y = int(input())
        print(x % y)
        # print("works 5")

    else:
        print("Invalid Operation")

    a = int(input())

# for i in ansArr:
#     print(i)

'''Calculator
Send Feedback
Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
3. If the input is 3, then 2 integers are taken from the user and their product is printed.
4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
6. If the input is 6, then the program exits.
7. For any other input, then print "Invalid Operation".
Note: Each answer in next line.
Input format:
Take integers as input, in accordance to the description of the question.
Constraints:Reverse of a number
Send Feedback
Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

Input format :
Integer N
Output format :
Corresponding reverse number
Constraints:
0 <= N < 10^8
Sample Input 1 :
1234
Sample Output 1 :
4321
'''

a = int(input())
Sum=0
while (a):
    num=a%10 # here we will get unit place's integer
    Sum=Sum*10+num
    a=a//10
print(Sum)

'''Palindrome number
Send Feedback
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
Sample Input 1 :
121
Sample Output 1 :
true
Sample Input 2 :
1032
Sample Output 2 :
false'''

#The error in your code is likely due to the fact that you are modifying the input number "num" in
# the "checkPalindrome" function, instead of using a separate variable to store the original input number.

def checkPalindrome(num):
    original_num = num
    reverse = 0
    # Implement Your Code Here
    while (num != 0):
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10
    return reverse == original_num


num = int(input())
isPalindrome = checkPalindrome(num)
if (isPalindrome):
    print('true')
else:
    print('false')

'''Sum of even & odd
Send Feedback
Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
Input format :
 Integer N
Output format :
Sum_of_Even_Digits Sum_of_Odd_Digits
(Print first even sum and then odd sum separated by space)
Constraints
0 <= N <= 10^8
Sample Input 1:
1234
Sample Output 1:
6 4
Sample Input 2:
552245
Sample Output 2:
8 15'''

# tried code
#variables val1 and val2 separaetd by space -print(val1, " ", val2)
# 12345
# 12345//10=1234
# 12345%10=5
# 0+5
# 1234//10=123
N= int(input())
sum_even=0
sum_odd=0
while (N!=0):
    a=N%10
    if (a%2==0):
        sum_even=sum_even+a
    else:
        sum_odd=sum_odd+a
    N=N//10

print(sum_even,sum_odd)
