num=int(input("Enter a Number:"))
sum=0
for i in range(1,num+1):
    n=num%10
    sum=sum+n
    num=num//10
   

print(sum)
    