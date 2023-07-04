def new_fruit(fruits):

    if fruits == '': #빈 문자열을 받으면 빈 리스트

        return []
    
    else:

        fruits = fruits.lower() #모든 문자를 소문자로 바꾸고

        fruit_list = fruits.split(',') #,를 기준으로 list로 만들고

        new_list = []

        for fruit in fruit_list:

            new_list.append(fruit.replace('rotten',''))
        
        return new_list


print(new_fruit('apple,rottenBanana,apple,RotTenorange,Orange'))


