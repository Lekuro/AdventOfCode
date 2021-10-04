with open('data.txt', 'r') as file1:
    data = file1.read()
# print(data)
data_list = data.split()
print(data_list)


class Ship:
    def __init__(self):
        self.moveE = 10
        self.moveN = 1
        self.shipE = 0
        self.shipN = 0

    def action(self, str_):
        letter = str_[0]
        if letter == 'F':
            value = int(str_[1:])
            self.shipE += self.moveE*value
            self.shipN += self.moveN*value
        elif letter == 'E':
            self.moveE += int(str_[1:])
        elif letter == 'W':
            self.moveE -= int(str_[1:])
        elif letter == 'N':
            self.moveN += int(str_[1:])
        elif letter == 'S':
            self.moveN -= int(str_[1:])
        else:
            value = int(str_[1:])
            if value >= 360:
                value %= 360
            if value == 0:
                return
            elif value == 180:
                self.moveE = -self.moveE
                self.moveN = -self.moveN
            elif value == 90:
                if letter == 'L':
                    self.moveN, self.moveE = self.moveE, -self.moveN
                if letter == 'R':
                    self.moveN, self.moveE = -self.moveE, self.moveN
            elif value == 270:
                if letter == 'L':
                    self.moveN, self.moveE = -self.moveE, self.moveN
                if letter == 'R':
                    self.moveN, self.moveE = self.moveE, -self.moveN


ship1 = Ship()
print('ship1.shipE', ship1.shipE)
print('ship1.shipN', ship1.shipN)
print('ship1.moveE', ship1.moveE)
print('ship1.moveN', ship1.moveN)
for item in data_list:
    print('item', item)
    ship1.action(item)
    print('ship1.shipE', ship1.shipE)
    print('ship1.shipN', ship1.shipN)
    print('ship1.moveE', ship1.moveE)
    print('ship1.moveN', ship1.moveN)
result_distance = abs(ship1.shipE)+abs(ship1.shipN)
print(result_distance)
