# Task 1: 
numbers = [1, 2, 3, 1, 4, 1, 5]
target = int(input("Enter a number to count its occurrences: "))
count = 0

for number in numbers:
    if number == target:
        count += 1

print(f"{target} appears {count} times.")
