#!/usr/bin/python3
numbers = 0
while numbers <= 89:
    if numbers % 10 == 0:
        numbers += 1 + numbers // 10
print("{:02d}".format(numbers), end='\n' if numbers == 89 else ", ")
numbers += 1
