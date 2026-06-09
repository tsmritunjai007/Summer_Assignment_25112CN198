n=int(input("Enter a number:"))
temporary=n
sum_fact=0
while temporary>0:
    digit=temporary%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum_fact+=fact
    temporary//=10

if sum_fact==n:
    print("Strong number")
else:
    print("Not a strong number")