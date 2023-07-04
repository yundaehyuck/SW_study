s = input()

word_list = s.split()

#대소문자 구분하지 않고 일치하면 끝말잇기를 한다고 보고 있으므로

if (word_list[0][-1].lower() == word_list[1][0].lower()) and (word_list[1][-1].lower() == word_list[2][0].lower()):

    print('Pass')

else:

    print('Fail')
