# Find the largest number in a list

numbers = [4, 7, 2, 9, 1]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
