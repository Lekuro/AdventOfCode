# get string from file 169
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
d_bags = {}
l_bags = []
magic = 'shiny gold'
for line in lines:
    parted_bag = line.split(' bags contain ')
    if parted_bag[1] == 'no other bags.':
        parted_bag[1] = ''
    l_bags.append(parted_bag)
    d_bags[parted_bag[0]] = parted_bag[1]


def print_bags():
    """
    print bags in list and bags like dict
    """
    print('------------------------------------')
    for bag in l_bags:
        print(bag)
    # for key in d_bags:
    #     print('key =', key, 'val =', d_bags[key])


print_bags()


def clean_bags():
    """
    line[1] partes by ', ' and replace other bag on 'shiny gold'
    """
    for line in l_bags:
        if '' == line[1] or line[0] == 'shiny gold':
            continue
        parted_kinds = line[1].split(', ')
        for index in range(len(parted_kinds)):
            #print('line[1]', line[1])
            parted = parted_kinds[index].split()
            # count = int(parted[0]), count
            # print(parted)
            parted = parted[1:-1]
            # print(parted)
            key = ' '.join(parted)
            #print('key', key)
            if key != 'shiny gold':
                parted_kinds[index] = d_bags[key]
            # print(parted_kinds[index])
        # print(parted_kinds)
        if all([i == '' for i in parted_kinds]):
            line[1] = ''
        else:
            line[1] = ', '.join(parted_kinds)
        while ', , ' in line[1]:
            line[1] = line[1].replace(', , ', ', ')
        if line[1][-2:] == ', ':
            line[1] = line[1][:-2]
        if line[1][:2] == ', ':
            line[1] = line[1][2:]


def check_bags():
    """
    line[1] partes by ', ' and looks for other bag than 'shiny gold' 
    return: True if there is other bag than shiny gold
    return: False if there are only shiny gold
    """
    for line in l_bags:
        if '' == line[1] or line[0] == 'shiny gold':
            continue
        parted_kinds = line[1].split(', ')
        for index in range(len(parted_kinds)):
            parted = parted_kinds[index].split()
            # count = int(parted[0])
            # print(parted, count)
            parted = parted[1:-1]
            # print(parted)
            key = ' '.join(parted)
            if key != 'shiny gold':
                return True
    return False


while check_bags():
    clean_bags()
    # print_bags()
    print('i work hard')

# amount of 'shiny gold'
count = 0
for line in l_bags:
    if '' == line[1] or line[0] == 'shiny gold':
        continue
    if 'shiny gold' in line[1]:
        count += 1
print(count)
print_bags()
print(count)
