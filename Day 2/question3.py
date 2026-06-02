n=int(input("Enter a number:"))

p=1

while n!=0:
    d=n%10
    p=p*d
    n=n//10

print("Product of digits=",p)