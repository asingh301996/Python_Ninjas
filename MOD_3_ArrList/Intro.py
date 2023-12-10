#     0,1,2,3,4
li = [5,6,7,8,5]
for i in range (1,4):         #if it was like print(i) then the output hve been different but it should be li[i]
    print(li[i], end='')

    #or

#     0,1,2,3,4
li = [5,6,7,8,5]
for i in li[1:4]:     #Here we have given list itself as a range so it will act acc. to the indexes in list
    print(i, end='')

#*****************************************************************************************************************
'''INPUT TO A LIST IN LINE SEPARATED FORMAT'''
l1=[]
n=int(input())
for i in range (n):
    curr=input()         # if it is in form of string then o/p =['12', '67']
    #curr = int(input())  #if it's in form of int then o/p =[12, 67]
    l1.append(curr)
print(l1)
print(type(l1))
# for ele in l1:
#     print(ele)


#---------------------------------------------------------------------
'''INPUT TO A LIST IN Space Separated FORMAT'''

# n=int(input())
# for i in range n:
#



'''SPLIT FUNCTION'''
string=input()
print (string)
#print(string.split(' '))  #this is splitting the string on basis of space between the characters of string o/p= ['2', '3', '6']
split_str= string.split(',')  #same as above just i/p will be comma included (2,3,4) o/p=['2', '3', '4']
print(split_str)
# therefore, splitting functionality works on basis of a delimiter
'''**** Now, if I want a list of integer not a string ***** '''
list=[]
for ele in split_str:
    list.append(int(ele))
print(list)

'''This all could be written in just one line'''

list = [int(x) for x in input().split()]  # this will give list of integers
print (list)





'''x=“8438388382352627378229”
   y=“4737356228834636373737”
   find sum = x+y '''


