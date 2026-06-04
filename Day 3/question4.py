a=int(input("enter the first number: "))
b=int(input("Enter the second number:"))

for i in range(max(a,b),a*b+1):
    if i%a==0 and i%b==0:
        print(i)
        break