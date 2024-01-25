# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/24/2024
# Description: Project 3b

num = int(input("Please enter a positive integer: "))
facts = []

for i in range(1, num//2+1):
    if num % i == 0:
        facts.append(i)

facts.append(num)

print("The factors of " + str(num) + " are: ")
print(*facts, sep = "\n")
