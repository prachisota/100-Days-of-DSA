#pallindrome number
# a number is said to be pallindrome if it is the same number when reversed
n=int(input("enter the number"))
rev=0
old=n
#need a container to hold old number to check later
while n>0:
    digit=n%10
    n=n//10
    rev=rev*10+digit
if rev==old:
    print("The number is pallindrome")
else:
    print("The number is not pallindrome")
    
'''another approach to solve pallindrome problem
is to check each digit at end and at beginning sim,multaneously
if number of deigits is even it would equally split
else if the number of digits is odd we will leave it as it would be
same digit from both sides'''

n=input("enter the number")
rev=n[::-1]
#reverses the string completely
if n==rev:
    print("the number is pallindrome")
else:
    print("the number is not pallindrome")

#-----------
m=input("enter the number")
flag=0
#to check if break statement was implemented or not
for i in range(len(m)//2):
    if m[i]!=m[len(m)-i-1]:
        print("The number is not Pallindrome")
        flag=1
        break
if flag!=1:
    print("The number is Pallindrome")





