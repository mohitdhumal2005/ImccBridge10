flag=0
num=int(input("Enter num:"))
for i in range(2,(num//2)+1):
    if (num%i==0):
        flag=1
        break
    
if(flag==0):
    print("Prime Number!")
else:
    print("Not Prime!")