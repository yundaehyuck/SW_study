#첨부파일

blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_dict = {}

for blood in blood_types:

    blood_dict[blood] = blood_dict.get(blood,0) + 1

print(blood_dict)
