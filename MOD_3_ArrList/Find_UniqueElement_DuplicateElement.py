'''Problem Statement:

Given is an array of size [2 * M + 1].

There are M Elements that are present twice.

Only one element is present once.

Constraints
1<=t<=10^2
0<=N<=10^3

Return that Singular Element.'''

######### XOR METHOD ################
li=[2,3,1,6,3,6,2]
result = li[0]
for i in range (1,len(li)):
    result= result ^ li[i]
print (result)

######## SET() METHOD ############

arr=[2,3,1,6,3,6,2]
    unique_ele = set()
    for i in range(len(arr)):
        if arr[i] not in unique_ele:
            unique_ele.add(arr[i])
        else:
            unique_ele.remove(arr[i])
    return unique_ele.pop().  # it's because neither add or remove mwthod returns anything pop
                              # will give you the value which was left in the set and you will get your unique_element this way




'''Problem Statement:

Given is an array of size [2 * M + 1].

There are M Elements that are present twice.

Only one element is duplicate one.

Constraints
1<=t<=10^2
0<=N<=10^3

Return that Duplicate Element'''



def duplicateNumber(arr, n) :
    #Your code goes here
    unique_ele=set()
    duplicates=set()
    for i in range (len(arr)):
        if arr[i] in unique_ele:
            duplicates.add(arr[i])
            #print ("D",duplicates)
        else:
            unique_ele.add(arr[i])
            #print("U",unique_ele)
    #return duplicates # so now, i am getting an error becuase it's returninga set and we want integer value so now we will chnage a bit of logic here
    if duplicates:
        return duplicates.pop()
    else:
        return None # to show if there are no duplicates present
