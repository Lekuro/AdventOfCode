with open('data.txt', 'r') as file1:
    data = file1.read()
print(data)
spited = data.split()
print(spited)
time = int(spited[0])
print('time', time)
buses = spited[1].split(',')
print('buses', buses)
buses = list(filter(lambda bus: bus != 'x', buses))
buses = list(map(lambda bus: int(bus), buses))
print('buses', buses)
# for item in range(time-10, time+10):
#     times = [item]
#     for bus in buses:
#         times.append('D' if item % bus == 0 else '')
#     print(times)
got = ''
for item in range(time, time+max(buses)):
    times = [item]
    for bus in buses:
        is_bus = 'D' if item % bus == 0 else ''
        times.append(is_bus)
        if is_bus == 'D':
            got = (item - time)*bus
    print(times)
    if got:
        print(got)
        break
