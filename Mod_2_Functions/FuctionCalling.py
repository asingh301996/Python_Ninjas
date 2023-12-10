'''


'''
# def C():
#     print('CS')
#     print('CE')
# def B():
#     print('BS')
#     C()
#     print('BE')
# def A():
#     print('AS')
#     B()
#     print('AE')
# A()
arr=[2,3,4,10]
target=6
#print(len(arr))

mid_val = len(arr) // 2
while mid_val<=len(arr) and mid_val>=0:
    #print(arr[mid_val])


    if arr[mid_val]==target:
         print(arr[mid_val], "found")
         break

    elif arr[mid_val]<target:
#[1,2,3,4,5,6,7,8,9]
        mid_val= mid_val+(mid_val//2)

    elif arr[mid_val]>target:
        mid_val=mid_val-((mid_val//2)+1)










#print(arr[mid_val])












#2,3,4,10,40