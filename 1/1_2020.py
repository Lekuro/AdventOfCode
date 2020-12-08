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
# choose two numbers
num1 = 0
num2 = 0
for i in numbers:
    for j in numbers:
        if i == j:
            continue
        #print(i, j)
        if i + j == 2020:
            num1 = i
            num2 = j
            break
#print(num1, num2)
product = num1 * num2
print(product)
