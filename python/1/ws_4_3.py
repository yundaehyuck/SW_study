
def remove_num_list(int_list):

    remove_list = []

    for num in int_list:

        try:

            if remove_list[-1] == num:

                pass
            
            else:
                remove_list.append(num)
        
        except:

            remove_list.append(num)
    
    return remove_list

print(remove_num_list([1,1,3,3,0,1,1]))

print(remove_num_list([2,2,2,2,2,2,2]))

print(remove_num_list([3,3,3,2,1,4,2,1,1,1,4,5,5,0,1,9,9,4]))

        
