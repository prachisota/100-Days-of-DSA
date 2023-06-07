#check if the array is sorted or not
#method 1 : brut force make a sorted array and check if they are equal
array=[1,2,3,3,6,7,8,9]
print(array==sorted(array))

#method 2: to make to variables/ pointers and check 
#if the left one is less than equal to the right one
'''
Assumptions made :
1. the array has atleast 2 elements
2. 2 cases with and without repititions of elements
'''
#here instead of taking 2 pointers i have take 1 pointer only
flag=1
for i in range(0,len(array)-1,1):
    if not array[i]<=array[i+1]:
        flag=0
        break
if flag==1:
    print(True)
else:
    print(False)
