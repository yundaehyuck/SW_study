
def sum_of_repeat_number(num_list):

    num_dict = {}

    for num in num_list:

        num_dict[num] = num_dict.get(num,0) + 1
    
    num_sum = 0

    for num,cnt in num_dict.items():

        if cnt == 1:

            num_sum += num
    
    return num_sum


print(sum_of_repeat_number([4,4,7,8,10,4]))
