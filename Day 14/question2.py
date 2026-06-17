n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

key = int(input("Enter the element whose frequency is to be found: "))

count = 0

for num in arr:
    if num == key:
        count += 1

print("Frequency of", key, "=", count)