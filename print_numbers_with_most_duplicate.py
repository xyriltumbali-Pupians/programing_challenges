nums = []

while True:
    n = input("Enter number: ")
    if not n.isdigit():
        break
    nums.append(int(n))

most = nums[0]
max_count = 0

for n in nums:
    c = nums.count(n)
    if c > max_count:
        max_count = c
        most = n

print(most)