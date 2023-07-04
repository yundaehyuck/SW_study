
participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

part_dict = {}

for part in participants:

    part_dict[part] = part_dict.get(part,0) + 1

for key,value in part_dict.items():

    if value == 1:

        print(key)
        break

