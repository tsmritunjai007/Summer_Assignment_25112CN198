n=int(input("Enter the number:"))
while n%2==0:
    last_factor=2
    n//=2

i=3
while i*i<=n:
    while n%i==0:
        last_factor=i
        n//=i
    i+=2
if n>2:
    last_factor=n   
print("Largest prime factor is:",last_factor)