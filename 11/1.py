def print_matrix(matrix):
    for line in matrix:
        print(line)
    print('-------------matrix end------------------')


def join_matrix(matrix):
    list_ = []
    for line in matrix:
        list_.append(''.join(line))
    return '\n'.join(list_)


def get_matrix(str_):
    lines = str_.split()
    matrix = []
    for line in lines:
        matrix.append(list(line))
    return matrix


def check8condition():
    count = 0
    if r > 0 and c > 0 and data_list[r-1][c-1] == '#':
        count += 1
    if r > 0 and data_list[r-1][c] == '#':
        count += 1
    if r > 0 and c+1 < cols and data_list[r-1][c+1] == '#':
        count += 1
    if c+1 < cols and data_list[r][c+1] == '#':
        count += 1
    if r+1 < rows and c+1 < cols and data_list[r+1][c+1] == '#':
        count += 1
    if r+1 < rows and data_list[r+1][c] == '#':
        count += 1
    if r+1 < rows and c > 0 and data_list[r+1][c-1] == '#':
        count += 1
    if c > 0 and data_list[r][c-1] == '#':
        count += 1
    return count


# get string from file
lines = []
with open('data.txt', 'r') as file:
    data = file.read()
print(data)

# get rows and cols
lines = data.split()
# print(lines)
rows = len(lines)
cols = len(lines[0])
print('cols', cols, 'rows', rows)
data_list = get_matrix(data)

# go through matrix
while True:
    is_change = False
    new_data = []
    r = 0
    c = 0
    for r in range(rows):
        new_line = []
        for c in range(cols):
            if data_list[r][c] == 'L':
                count = check8condition()
                if count == 0:
                    new_line.append('#')
                    is_change = True
                else:
                    new_line.append(data_list[r][c])
            elif data_list[r][c] == '.':
                new_line.append(data_list[r][c])
            elif data_list[r][c] == '#':
                count = check8condition()
                if count >= 4:
                    new_line.append('L')
                    is_change = True
                else:
                    new_line.append(data_list[r][c])
        new_data.append(new_line)
    data_str = join_matrix(new_data)
    #print(data_str, '\n')
    print('i still work')
    data_list = get_matrix(data_str)
    if not is_change:
        break

print('result', data_str.count('#'))
