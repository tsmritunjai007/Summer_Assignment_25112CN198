x=int(input("Enter a base:"))
n=int(input("Enter exponent:"))

result=1
for i in range(n):
    result*=x
print("Result:",result)