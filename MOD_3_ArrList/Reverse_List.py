'reversing the list '

def reverseList(li):
    len_li=len(li)
    for i in range (len_li//2):  # because i will swap the digits till half the length of list
        b=li[i]
        li[i]= li[len_li-i-1]
        li[len_li - i - 1] = b

li=[2,3,4,9,6,7]
reverseList(li)
print(li)

#************  or  ******************
li=[2,3,4,9,6,7]
li=li[::-1]
print ("reversed new list",li)



li=[1,34,0,7,5,9]
z=li[3:1:-1]
print(z)

li=[1,34,0,7,5,9]
z=li[:1:-1]  # here since I've not specified anything it will end at the last index of the list which is 5
print(z)

li=[1,34,0,7,5,9]
z=li[3::-1]
print(z)