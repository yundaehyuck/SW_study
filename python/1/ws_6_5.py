#반복문

def sum_of_digit(num):

    digit_sum = 0

    while 1:

        num,r = divmod(num,10)

        digit_sum += r

        if num < 10:

            break
    
    digit_sum += num

    return digit_sum


#반복문을 활용하지 않음

def sum_of_digit2(num):

    return sum(map(int,str(num)))

number = int(input('정수를 입력하세요. :'))

print('반복문:',sum_of_digit(number))
print('반복문을 쓰지 않음:',sum_of_digit2(number))
