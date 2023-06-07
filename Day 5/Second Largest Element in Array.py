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
'''This is the Brut Force Approach imagine doing this with a 
sorting algo of n**2 complexity or nlogn complexity but the other 
method is more optimised as it only takes O(n) '''

#what we missed in this is the case of repitive numbers for example:-
#array=[1,7,7,7,8,8,9,9]
#now with this we will have to check if there are no repittions

array=[1,7,7,7,8,8,9,9]
#first sort the array
new_array=sorted(array)
i=-1
max=new_array[-1]
second_max=new_array[-1]
while second_max==max:
    i-=1
    second_max=new_array[i]
print(second_max)

#but the worst case can be [1,7,7,7,7,7]
array=[1,2,8,8,8,7,7,7,7,7,7,7]
new_array=[]
for i in array:
    if i in new_array:
        continue
    else:
        if new_array==[] or i>new_array[-1]:
            new_array.append(i)
        elif i<new_array[0]:
            new_array=[i]+new_array
        else:
            j=0
            while i>new_array[j]:
                j+=1
            new_array=new_array[:j]+[i]+new_array[j:]
print(new_array[-2])
#assuming there are atleast 2 distinct elements in the array
            


