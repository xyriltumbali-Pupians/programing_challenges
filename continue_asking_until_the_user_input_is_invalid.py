numbers = []

while True:
    num = input("Enter a number: ")

    if not num.isdigit():
        break

    num = int(num)
    numbers.append(num)

    if numbers.count(num) == 1:
        print("Unique")
    else:
        print("Duplicate")