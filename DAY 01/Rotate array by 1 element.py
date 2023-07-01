#array rotation by 1 place:
array=[1,2,34,5,7,89,9,10]

#brute force approach
#Method 1:Array slicing
#left rotation is left most array is put back in the last most segment
array=array[1:]+array[:1]
print(array)

array=[1,2,34,5,7,89,9,10]
#method 2: duplicate array
arr2=[]
for i in range(1,len(array)):
    arr2.append(array[i]) 
for i in range(0,1):
    arr2.append(array[i])
array=arr2
print(array)

#but What if we have to do inplace array rotatio
#ANSWER
#we can store the first element in a container and then
# shift array from right to left
#and then copy paste the stored element

array=[1,2,34,5,7,89,9,10]
element=array[0]
for i in range(1,len(array)): #len(array ) for end as it is rotation
    array[i-1]=array[i]
array[i]=element
print(array)

