# get numbers from file
lines = []
with open('numbers.txt', 'r') as f:  # adventofcode/
    for line in f:
        # print(line)
        lines.append(line)
numbers = []
for item in lines:
    numbers.append(int(item))
# print(numbers)
# choose three numbers
num1 = 0
num2 = 0
num3 = 0
for i in numbers:
    for j in numbers:
        for e in numbers:
            if i == j or i == e or j == e:
                continue
            # print(i, j)
            if i + j + e == 2020:
                num1 = i
                num2 = j
                num3 = e
                break
print(num1, num2, num3)
product = num1 * num2 * num3
print(product)
