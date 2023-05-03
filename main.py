import re

# the first task

def to_camel_case(text):
    # to divide the string by words
    words = re.split(r'[-_]', text)
    # to transform if the first letter is uppercase
    if words[0].isupper():
        words[0] = words[0].capitalize()
    # to transform if the first letter isn't uppercase
    else:
        words[0] = words[0].lower()
    # to transform other words
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()
    # to join all words together
    return ''.join(words)

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))

# the second task

def get_directions(start, end):
    # to set the start and the end of a walk
    start_split = start.split(' ')
    start_avenue = int(start_split[0].replace('th', ''))
    start_street = int(start_split[4].replace('th', ''))
    start_direction = start_split[2]

    end_split = end.split(' ')
    end_avenue = int(end_split[0].replace('th', ''))
    end_street = int(end_split[4].replace('th', ''))
    end_direction = end_split[2]

    # to calculate how much blocks a user need to go
    blocks_north_south = abs(end_street - start_street)
    blocks_east_west = abs(end_avenue - start_avenue)

    # to set a direction
    ns_direction = 'north' if end_street > start_street else 'south'
    ew_direction = 'east' if end_avenue > start_avenue else 'west'

    # to generate instructions for user
    directions = f"Walk {blocks_north_south} blocks {ns_direction}, and {blocks_east_west} blocks {ew_direction}"

    return directions

start = "8th Ave and W 38th St"
end = "7th Ave and W 36th St"
print(get_directions(start, end))

start = "5th Ave and E 46th St"
end = "7th Ave and W 58th St"
print(get_directions(start, end))
