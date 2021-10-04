with open('data.txt', 'r') as file1:  # ni data.txt
    data = file1.read()
print(data)
spited = data.split()
print(spited)
time = int(spited[0])
print('time', time)
buses = spited[1].split(',')
print('buses', buses)
buses_index = []
for index in range(len(buses)):
    if buses[index] != 'x':
        buses_index.append((int(buses[index]), index))
print('buses_index', buses_index)
max_pair = buses_index[0]
for pair in buses_index:
    if max_pair[0] < pair[0]:
        max_pair = pair
print(max_pair)
buses = list(filter(lambda bus: bus != 'x', buses))
buses = list(map(int, buses))
base_ = 100000000000000  # max(buses) + 1
step_ = max(buses)
key = max_pair[1]
for i in range(base_*base_):
    if base_ % step_ != 0:
        base_ += 1
    else:
        break
buses_len = len(buses)
#generator1 = (i for i in range(base_, 110000000000000, step_))  #
# for num in generator1:
while base_ < 101000000000000:
    count = 0
    #number = num - key
    number = base_ - key
    for pair in buses_index:
        # print(pair)
        if (number+pair[1]) % pair[0] == 0:
            count += 1
        else:
            break
    if count == buses_len:
        print(number)
        break
    base_ += step_
