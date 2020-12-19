# get string from file
lines = []
with open('data.txt', 'r') as file:
    for line in file:
        if line[-1:] == '\n':
            lines.append(line[:-1])
        else:
            lines.append(line)
# print(lines)

# part by ' bags contain ' create dict with key like name of bags, value is everything else
# and list of all bags first part name of bags second is everything else
d_bags = {}  # dict with unigue bags
magic = 'shiny gold'
for line in lines:
    parted_bag = line.split(' bags contain ')
    if parted_bag[0] == magic:
        # it is list of bags inside shiny gold bag
        l_bags = parted_bag[1].split(', ')
        l_bags[-1] = l_bags[-1][:-1]
    d_bags[parted_bag[0]] = parted_bag[1]


def print_bags():
    """
    print bags like dict and shiny gold bags 
    """
    print('------------------------------------')
    print('Magic bag', l_bags)
    # for key in d_bags:
    #     print('key =', key, 'val =', d_bags[key])


print_bags()


def part_bag():
    """
    function go through l_bags and split(', ') every element
    """
    index = 0
    while index < len(l_bags):
        if ', ' in l_bags[index]:
            bags = l_bags[index].split(', ')
            # print(bags)
            l_bags[index:index + 1] = bags
            # print(l_bags)
        index += 1
    print('----part_bag------')


def check_bag():
    '''
    function go through l_bags and look for bags
    return: True if find something else than 'no other bags'
    return: False if there is no bags
    '''
    for bag in l_bags:
        if bag != 'no other bags':
            return True
    return False


counter = 0
# for i in range(7):
while check_bag():
    print('check_bag()', check_bag())
    # this loop takes a bag, parts it and gets the key,
    # look for key in d_bags contained bags
    # and insert finded bags for place of this bag
    for index in range(len(l_bags)):
        if l_bags[index] == 'no other bags':
            continue
        #print('l_bags[index] =', l_bags[index])
        parted = l_bags[index].split()
        count = int(parted[0])
        counter += count
        #print('parted =', parted, 'count =', count)
        key = ' '.join(parted[1:-1])
        #print('key =', key)
        if key != 'shiny gold':
            l_bags[index] = d_bags[key] * count
            if l_bags[index][-1] == '.':
                l_bags[index] = l_bags[index][:-1]
            if '.' in l_bags[index]:
                l_bags[index] = l_bags[index].split('.')
                l_bags[index] = ', '.join(l_bags[index])
        # print('l_bags[index] =', l_bags[index])
        # print_bags()
    print('finish deeper')
    # print_bags()
    part_bag()
    # print_bags()
    print('lenght of magic:', len(l_bags))
    print('counter', counter)
