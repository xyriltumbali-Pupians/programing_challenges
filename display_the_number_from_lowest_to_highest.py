nums = []

while True:
    n = input("Enter number: ")
    if not n.isdigit():
        break
    nums.append(int(n))

nums.sort()
print(nums)