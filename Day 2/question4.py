n=int(input("Enter the number:"))

o=n
reverse=0
while n!=0:
    d=n%10
    reverse=reverse*10+d
    n=n//10

if o==reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")    
