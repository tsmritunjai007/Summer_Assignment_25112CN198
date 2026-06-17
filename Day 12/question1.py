def palindrome(n):
    return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))

if palindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")