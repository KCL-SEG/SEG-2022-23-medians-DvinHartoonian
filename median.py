"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

for i in range(0, len(numbers) - 1):
    for j in range(len(numbers) - 1):
        if(numbers[j] > numbers[j+1]):
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp



median = 0

if len(numbers) == 1:
    median = numbers[0]
elif len(numbers) % 2 == 0:
    median = (numbers[(len(numbers) // 2) - 1] + numbers[(len(numbers) // 2)]) / 2
else:
    median = numbers[(len(numbers)) // 2]
print(median)
