'''Functions are defined as a method which includes
 the logic and you can use that func. by calling it directly'''
    # nCr = n!/r!(n-r)!
    # 3C2= 3!/2!(3-2)!

factorial  Calculation
n = int(input("value of n="))
r= int(input("value of r="))

n_fact=1                  #1 to 4 --> 1,2,3= 1,2 & 6
for i in range (1,n+1):
    n_fact=n_fact*i
    #print("n!",n_fact)

r_fact=1
for i in range (1,r+1):  #1 to 3--> 1 & 2 = 1,2
    r_fact=r_fact*i
    #print("r",r_fact)

n_r_fact=1               #1 to 2 -->                                                                                                                                                                   3-2 =1
for i in range (1,n-r+1):
    n_r_fact =n_r_fact*i
    #print(n_r_fact)

ans = n_fact//(r_fact * n_r_fact)
print(ans)

''' Alternative '''

def fact (a):
     a_fact= 1
     for i in range (1, a+1):
         a_fact=a_fact *i
     return a_fact
n=int(input("enter value of n"))
r=int(input("enter value of r"))
n_fact= fact(n)
r_fact= fact(r)
n_r_fact=fact(n-r)
ans = n_fact//(r_fact * n_r_fact)
print(ans)
