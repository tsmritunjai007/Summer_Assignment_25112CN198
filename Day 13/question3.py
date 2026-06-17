n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = max(arr)
smallest = min(arr)

print("Array:", arr)
print("Largest element =", largest)
print("Smallest element =", smallest)