import re
# get numbers from file
with open('data.txt', 'r') as f:  # 04/
    lines = []
    part = ''
    for line in f:
        # print(line)
        if line == '\n':
            lines.append(part)
            part = ''
        else:
            part += line + ' '
    if part != lines[-1] and part != '':
        lines.append(part)
# print(lines)

# take passport like a dict
passports = []
for i in lines:
    line = i.split()
    # print(line)
    line_splite = []
    for j in line:
        line_splite.append(j.split(':'))
    passports.append(dict(line_splite))
# print(passports)

# task1 chose passports with 8 fields and 7 without 'cid' field
task1_data = []
for pas in passports:
    if len(pas) == 8:
        task1_data.append(pas)
    elif len(pas) == 7 and 'cid' not in pas:
        task1_data.append(pas)
# for i in task1_data:
#     print(i)
# print(task1_data)
print(len(task1_data))

# task2
valid_passport = []
for pas in task1_data:
    counter = 0
    # print(pas)
    if re.findall(r"[0-9]{4}", pas['byr']) and 1920 <= int(pas['byr']) and int(pas['byr']) <= 2002:
        counter += 1
    if re.findall(r"[0-9]{4}", pas['iyr']) and 2010 <= int(pas['iyr']) and int(pas['iyr']) <= 2020:
        counter += 1
    if re.findall(r"[0-9]{4}", pas['eyr']) and 2020 <= int(pas['eyr']) and int(pas['eyr']) <= 2030:
        counter += 1
    if pas['hgt'][-2:] == 'cm' and 150 <= int(pas['hgt'][:-2]) and int(pas['hgt'][:-2]) <= 193:
        counter += 1
    # = =
    if pas['hgt'][-2:] == 'in' and 59 < int(pas['hgt'][:-2]) and int(pas['hgt'][:-2]) < 76:
        counter += 1
    if pas['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        counter += 1
    if re.findall(r"[0-9]{9}", pas['pid']):
        counter += 1
    if re.findall(r"#[0-9a-f]{6}", pas['hcl']):
        counter += 1
    if counter == 7:
        valid_passport.append(pas)

# for pas in valid_passport:
#     print(pas)
print(len(valid_passport))
