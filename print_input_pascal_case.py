name = input("Enter your full name: ")
words = name.split()
print("".join(word.capitalize() for word in words))