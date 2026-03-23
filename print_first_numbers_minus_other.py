nums = []

for i in range(10):
    nums.append(int(input("Enter number: ")))

result = nums[0]

for n in nums[1:]:
    result -= n

print(result)