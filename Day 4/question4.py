start=int(input("Enter starting of range:"))
end=int(input("Enter ending of range:"))

for n in range(start,end+1):
    temporary=n
    num_digits=len(str(n))
    sum=0
    while temporary>0:
        digit=temporary%10
        sum=sum+digit**num_digits
        temporary=temporary//10

    if sum==n:
        print(n)