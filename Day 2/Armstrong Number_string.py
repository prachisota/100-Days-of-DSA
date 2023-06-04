#Armstrong Number using Integers
#an armstrong number is the number which is equal to the sum of the cubes of its digits
#eg: 3^3+7^3+1^3=371 which is armstrong number
n=input("enter the number: ")
#this will store the number as a string for easy traversal
sum=0
#WE Do not need A CONTAINER TO HOLD THE VAL23UE as string is immmutable
for i in n:
    sum+=int(i)**3
#i=digit
if sum==int(n):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
