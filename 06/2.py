import re
# get data from file
with open('data.txt', 'r') as f:  # _example
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
    line = line.split('\n')
    if line[-1] == '':
        del line[-1]
    datas.append(line)
print(datas)

# transform data to list of set
answers = []
for data in datas:
    group = []
    for i in data:
        group.append(set(i))
    answers.append(group)
print(answers)

# count answers of group
count = 0
for answer in answers:
    i = 1
    set_ = answer[0]
    print(set_)
    for i in range(len(answer)):
        set_ = set_.intersection(answer[i])
    count += len(set_)
print(count)
