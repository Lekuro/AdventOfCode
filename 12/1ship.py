with open('data.txt', 'r') as file1:
    data = file1.read()
# print(data)
data_list = data.split()
print(data_list)


class Ship:
    directions = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

    def __init__(self):
        self.direction = 'E'
        self.direction_value = 0
        self.moveE = 0
        self.moveN = 0

    def action(self, str_):
        if str_[0] == 'F':
            if self.direction == 'E':
                self.moveE += int(str_[1:])
            elif self.direction == 'W':
                self.moveE -= int(str_[1:])
            elif self.direction == 'N':
                self.moveN += int(str_[1:])
            elif self.direction == 'S':
                self.moveN -= int(str_[1:])
        elif str_[0] == 'E':
            self.moveE += int(str_[1:])
        elif str_[0] == 'W':
            self.moveE -= int(str_[1:])
        elif str_[0] == 'N':
            self.moveN += int(str_[1:])
        elif str_[0] == 'S':
            self.moveN -= int(str_[1:])
        else:
            value = int(str_[1:])
            if value >= 360:
                value %= 360
            if str_[0] == 'L':
                self.direction_value += value
            elif str_[0] == 'R':
                self.direction_value -= value
            if self.direction_value < 0:
                self.direction_value += 360
            if self.direction_value >= 360:
                self.direction_value %= 360
            self.direction = Ship.directions[self.direction_value]


ship1 = Ship()
print('ship1.moveE', ship1.moveE)
print('ship1.moveN', ship1.moveN)
print('ship1.direction', ship1.direction)
print('ship1.direction_value', ship1.direction_value)
for item in data_list:
    print('item', item)
    ship1.action(item)
    print('ship1.moveE', ship1.moveE)
    print('ship1.moveN', ship1.moveN)
    print('ship1.direction', ship1.direction)
    print('ship1.direction_value', ship1.direction_value)
result_distance = abs(ship1.moveE)+abs(ship1.moveN)
print(result_distance)
