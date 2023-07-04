
#첨부파일

words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

#우리말 번역은 보지않으면 반의어로 바꿀수가 없으니까
#단어만 규칙에 맞게 반의어로

ant_words_list = []

for key in words_dict:

    if key[0] in ['p','m','b']:

        ant_words_list.append('im'+key)
    
    elif key[0] == 'l':

        ant_words_list.append('il'+key)
    
    elif key[0] == 'r':

        ant_words_list.append('ir'+key)

ant_words_list.sort() #오름차순 정렬

print(ant_words_list)
