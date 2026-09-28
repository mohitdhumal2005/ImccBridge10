num=int(input("Enter number:"))
rev=0
temp=num
while temp>0:
    n=temp%10
    rev=rev*10+n
    temp=temp//10

if rev==num:
    print("Palindrome")
else:
    print("Not Palindrome")