
fruit_str = input('과일봉지를 입력하세요 : ')

if fruit_str == '':

    print([])

else:

    fruit_list = fruit_str.lower().split(',')

    for ind,fruit in enumerate(fruit_list):

        if 'rotten' in fruit:

            fruit_list[ind] = fruit_list[ind][6:]
    
    print(fruit_list)

