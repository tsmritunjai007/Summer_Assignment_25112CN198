n=int(input("Enter a number:"))
temporary=n
num_digits=len(str(n))
sum=0
while temporary>0:
    digit=temporary%10
    sum=sum+digit**num_digits
    temporary=temporary//10

if sum==n:
    print("Armstrong number")
else:
    print("Not a armstrong number")