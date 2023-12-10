'''Array Sum
Given an array of length N, you need to find and print the sum of all elements of the array.
Input Format :
Line 1: An Integer Ni.e. size of array
Line 2: N integers which are elements of the array, separated by spaces
Output Format :
Sum
Constraints :
1＜=N <=10へ6
Sample Input :
3
9 8 9
Sample Output :
26'''

n= int(input())
list1= [int(x)for x in input().split()]
result=0
for ele in list1:
    result=result+ele
print (result)

'''x=“8438388382352627378229”
   y=“4737356228834636373737”
   find sum = x+y '''

def sum(x,y):
    #first step is to see whether the string is of same length or not
    x,y=strSizeCompare(x,y)
    carry=0
    result=''
    for i in range (len(x)-1, -1,-1):  # index starts from 0 to n '2[0],3[1],4[2],5[3],7[4],9[5]'
        sum= int(x[i])+int(y[i])+ carry
        result= str(sum%10) +result
        carry= sum//10
    if (carry!=0):
        result=str(carry)+result
    return result

def strSizeCompare(x,y):
    x_len=len(x)
    y_len=len(y)
    if (y_len<x_len):
        y=zeroPadding(y,x_len)  # so y= 000238
    else:
        x=zeroPadding(x,y_len)
    return x,y

def zeroPadding(small_no,len_largeNo):
    small_no_len= len(small_no)
    while (small_no_len!= len_largeNo):
        small_no='0' + small_no
        small_no_len=small_no_len+1
    return small_no

x='8438388382352627378229'
y='4737356228834636373737'
z=sum(x,y)
print(z)

