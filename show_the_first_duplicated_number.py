num1 = int(input("No 1.Please insert your number here"))
num2 = int(input("No 2.Please insert your number here"))
num3 = int(input("No 3.Please insert your number here"))
num4 = int(input("No 4.Please insert your number here"))
num5 = int(input("No 5.Please insert your number here"))
num6 = int(input("No 6.Please insert your number here"))
num7 = int(input("No 7.Please insert your number here"))
num8 = int(input("No 8.Please insert your number here"))
num9 = int(input("No 9.Please insert your number here"))
num10 = int(input("No 10.Please insert your number here"))

numbers = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

print("\nAll numbers:")
for n in numbers:
    print(n)

print("Numbers without duplicates:")

unique_numbers = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print(unique_numbers)