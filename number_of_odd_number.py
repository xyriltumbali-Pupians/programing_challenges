nums = []

for i in range(10):
    nums.append(int(input("Enter number: ")))

count = 0
for n in nums:
    if n % 2 != 0:
        count += 1

print(count)