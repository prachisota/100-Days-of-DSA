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
