#remove duplicates in place from a sorted array 
#that is you have to modif ythe given array and not create another array
#like in array=[1,1,1,2,2,3,4,5] unique elements are 1,2,3,4,5 so array has to
# be modified as [1,2,3,4,5,_,_,_] as we dont care about the remaining elements
#we make 2 pointer and as soon as we see different element we exchange them 
#first pointer being right after unique elements and anothrer traversing the array
array=[1,1,1,2,2,3,4,5]
i=1 #as 1st element is always unique
j=1
for j in range(1,len(array),1):
    if array[j] not in array[:i]:
        array[i],array[j]=array[j],array[i]
        i+=1
    else: pass
print("no of unique elements: ", i)
