answer = 7

chance = 0

while chance < 3:

    guess = int(input('0~9까지 비밇번호를 입력하세요(최대 3번 반복 가능) : '))

    chance += 1

    if guess == answer:

        print('정답입니다.')

        break
    
    else:

        if chance == 3:
            
            print("3번안에 맞추지 못했습니다.")
        
        else:

            print(f'다시 입력하세요. {3-chance}번 남았습니다.')
