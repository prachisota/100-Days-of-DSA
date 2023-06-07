#to find 2nd largest Elemnt in the array
array=[1,2,44,66,7,8,9]# ans 44
#method 1 : Traversal
max=array[0]
second_max=0#will get updated in the future
for i in array:
    if i >max:
        second_max=max
        max=i
print(second_max)

#method 2:sorting
print(sorted(array)[-2])#second last element in the sorted array
''' This is the Brut Force Approach imagine doing this with a 
sorting algo of n**2 complexity or nlogn complexity but the other 
method is more optimised as it only takes O(n) '''
