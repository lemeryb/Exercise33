# Title: Exercise 33
# Author: Benjamin Lemery
# Date: 10/14/19
# This program is designed to demonstrate the use of while loops.

i = 0
numbers = []

while i < 6:
    print(f"At the top is is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)