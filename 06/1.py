import re
# get data from file
with open('data.txt', 'r') as f:  # 04/ adventofcode/
    lines = []
    part = ''
    for line in f:
        # print(line)
        if line == '\n':
            lines.append(part)
            part = ''
        else:
            part += line
    if part != lines[-1] and part != '':
        lines.append(part)
print(lines)

# take data like a list
datas = []
for line in lines:
    line = line.replace('\n', '')
    datas.append(line)
print(datas)

# transform data to unigue
answers = []
for data in datas:
    data = set(data)
    answers.append(data)
print(answers)

# count unigue answers
count = 0
for answer in answers:
    count += len(answer)
print(count)
