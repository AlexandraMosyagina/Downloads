def unique_string(strings):
    unique_strings = []
    for i in strings:
        unique_str = ''
        for j in i:
            if j not in unique_str:
                unique_str += j
        unique_strings.append(unique_str)
    return unique_strings

