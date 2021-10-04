with open('data26e.txt', 'r') as file1:  # ni data.txt
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
buses = list(filter(lambda bus: bus != 'x', buses))
buses = list(map(int, buses))
base_ = max(buses)  # 100000000000000
step_ = buses[0]
for i in range(base_):
    if base_ % step_ != 0:
        base_ += 1
    else:
        break
generator1 = (i for i in range(base_, 110000000000000, step_))
# while True:
for number in generator1:
    buses_len = len(buses)
    count = 0
    for pair in buses_index:
        # print(pair)
        if (number+pair[1]) % pair[0] == 0:
            count += 1
        else:
            break
    if count == buses_len:
        print(number)
        break
