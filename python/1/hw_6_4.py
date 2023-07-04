
def group_anagrams(str_list):

    group_dict = {}

    for string in str_list:

        sort_string_list = sorted(string)

        sort_string = ''.join(sort_string_list)

        if group_dict.get(sort_string):

            group_dict[sort_string].append(string)
        
        else:

            group_dict[sort_string] = []
            group_dict[sort_string].append(string)
    

    return list(group_dict.values())

print(group_anagrams(['eat','tea','tan','ate','nat','bat']))
