def armstrong(n):
    num = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    return total == num

num = int(input("Enter a number: "))

if armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")