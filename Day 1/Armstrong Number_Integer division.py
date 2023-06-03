#Armstrong Number using Integers
#an armstrong number is the number which is equal to the sum of the cubes of its digits
#eg: 3^3+7^3+1^3=371 which is armstrong number
n=int(input("enter the number: "))
sum=0
#WE NEED A CONTAINER TO HOLD THE VALUE OF THE NUMBER TO CHECK IT LATER
c=n
while (n>0):
    digit=n%10
    n=n//10
    sum+=digit**3
    #adding the digits cube
if (c==sum):
    print("The Number is Armstrong")
else:
    print("The Number is not Armstrong")
