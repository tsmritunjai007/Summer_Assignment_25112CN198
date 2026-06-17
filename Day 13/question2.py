n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

total = sum(arr)
average = total / n

print("Array:", arr)
print("Sum =", total)
print("Average =", average)