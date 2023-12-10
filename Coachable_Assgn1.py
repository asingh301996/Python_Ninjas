# ELEMENTARY SORTING
# ** Selection and Insertion Sort
    #1. Selection Sort
def SelectionSort(b):
    if len(set(b))==1: #validate whether there's any repetition in the list and AVOID SWAPPING
        return b
    for i in range(0,len(b)):
        'I will have to find the min. value'
        print(i)
        for j in range (i+1,len(b)):
            'compare the no. here'
            if b[i]>b[j]:
                '''in PYTHON swapping works as :a,b=b,a
                which is concept to swap the values directly within the list
                '''
                # temp =b[i]
                # b[i]=b[j]
                # b[j]=temp
                b[i],b[j]=b[j],b[i]


a=[12,1,1,1,1,1]
SelectionSort(a)
print(a)

'''Tuple unpacking is a feature in Python that allows you to assign 
the values from a tuple (or any iterable) to multiple variables in a 
single line of code. It's a convenient way to simultaneously assign values 
to variables without the need for temporary variables or complex assignments'''

'''Using a set to validate whether there's any repetition in the list & to 
AVOID SWAPPING and getting into for loop unnecessarily
This is checking if the set of elements in b has a length of 1.'''


# 2. Insertion Sort

def InsertionSort(y):
    for i in range (0, len(y)):
        minval=0
        for j in range (i+1,len(y) ):
            





              i=3
x = [12, 7, 1, 3, 19, 13]
12>7
swap
7,12,1,3,19,13
12>1
swap
7,1,12.3.19.13

