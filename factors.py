# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/24/2024
# Description: Project 3b

num = int(input("Please enter a positive integer: "))
print("The factors of", num, "are:")

for factor in range(2, num):
    if num % factor == 0:
        print(factor)