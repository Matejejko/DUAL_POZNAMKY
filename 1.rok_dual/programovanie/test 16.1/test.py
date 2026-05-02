mix = ['jablko', 'oko', 'koleno', 1221, True, 59, 'AA', False, 'krk', '4354', 'kiwi', 53, 443, 'jablko']

def count_strings(mix):
    count = 0
    for item in mix:
        if isinstance(item, str):
            count += 1   
    return count
retazec = count_strings(mix)

shortest_string = None
for item in mix:
    if type(item) == str:
        if shortest_string is None or len(item) < len(shortest_string) or (len(item) == len(shortest_string) and item < shortest_string):
            shortest_string = item

sum = 0
for item in mix:
    if isinstance(item, (int, float)) and not isinstance(item, bool):
        sum += item
    elif isinstance(item, str) and item.isnumeric():
        sum += int(item) 

valid_numbers = []

### otras pardon ###
for item in mix:
    if isinstance(item, (int, float)):
        number = item
    elif isinstance(item, str) and item.isdigit():
        number = int(item)
    else:
        continue
    str_number = str(number)
    if len(str_number) > 2 and str_number[0] == str_number[-1]:
        valid_numbers.append(number)
if valid_numbers:
    najmensie = min(valid_numbers)
    najvacsie = max(valid_numbers)

###   koniec otrasu   ###


def remove_bool(mix):
    result = []
    for item in mix:
        if not isinstance(item, bool):
            result.append(item)
    return result
bool = remove_bool(mix)



print(f"1) Zoznam mix bez bool hodnot: {bool}")
print(f"2) Pocet retazcov v zozname mix je: {retazec}")
print(f"3) Najkratsi, nie numericky retazec je: {shortest_string}")
print(f"4) Sucet vsetkych cisel zoznamu mix je: {sum}")
print(f"Najmensie cislo s rovnakou zaciatocnou a koncovou cislocou je: {najmensie}  a najvacsie je {najvacsie}")
