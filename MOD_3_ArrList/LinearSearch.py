'''Let's say you have a list of some no. and you have been given a random number which you need to find in the list
and as an output you have to print it's index if teh number is found in the list'''

n=int(input())

list_1=[int(x) for x in input().split()]
print(list_1)
find_no= int(input())
flag= 0
for i in range (0, len(list_1)):
    if (list_1[i]==find_no):
        print(i)
        flag= 1
        break
    # else:              # you can't put else here because everytime the element is not found it will print -1
   #     print(-1)
print(flag)
if (flag==0):
    print(-1)

'''Linear Search - Through functions '''

def linearSearch(li,no):
    for i in range (0, len(li)):
        if (li[i]==no):
            return i
    return -1

li= [2,3,5,0]
result_index= linearSearch(li,0)
print(result_index)

def change (li):
    li[1] = li[1] + 2
    li = [3,3,3,4,5]
li = [1,2,3,4,5]
change (li)
print(li)






#
#
# li=['coder','fish','grapes','sit']
# # z=thirdGreatEle(li)
#
# max_len = -1
# for ele in li:
#     if len(ele) > max_len:
#         max_len = len(ele)
#         res = ele
# print("Maximum length string is : " + res)